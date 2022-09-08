import sys
import json
import ast

data = json.loads(ast.literal_eval(sys.argv[1]))
print(data)

with Path("rdp_news_submitted.json").open("w") as out_file:
    out_file.write(data)


