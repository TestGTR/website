# standard
import json
from os import getenv
from pathlib import Path

# 3rd party
from jinja2 import Environment, FileSystemLoader, select_autoescape

# variables
submitted_form_data: Path = Path("rdp_news_submitted.json")
issue_comment_template: Path = Path("issue_comment_rdp_template.jinja")

# load JSON from issue form
with submitted_form_data.open("r", encoding="UTF8") as in_json:
    data = json.load(in_json)

# complete data with environment vars
data["issue_author"] = getenv("ISSUE_AUTHOR", "Inconnu(e)")
data["issue_id"] = getenv("ISSUE_ID", "99999")

# handle legacy form keys id (- not supported)
new_keys=[k.replace("-", "_") for k in data.keys()]
data = dict(zip(new_keys, data.values()))

# fill the comment template
env = Environment(
    autoescape=select_autoescape(["html", "xml"]),
    loader=FileSystemLoader(Path(__file__).parent),
)

template = env.get_template(issue_comment_template.name)

# write to the output
with Path("rdp_news_submitted_comment_output.md").open("w", encoding="UTF8") as out_file:
    out_file.write(template.render(data))
