import re

def solve(value):
    return len(re.findall(re.escape(value["needle"]), value["text"])) if value["needle"] else 0
