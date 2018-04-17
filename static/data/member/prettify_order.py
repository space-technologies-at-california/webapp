import os
import json
import glob

members = glob.glob("*.json")
old = list(map(lambda x: (x, json.load(open(x))), members))

new = sorted([(x, y) for x, y in old if y["profile-order"] is not None], key=lambda x: x[1]["profile-order"])
new += sorted([(x, y) for x, y in old if y["profile-order"] is None], key=lambda x: x[1]["name"])

for i, n in enumerate(new):
    n[1]["profile-order"] = i + 1
    with open(n[0], "w") as f:
        json.dump(n[1], f, indent=2)
    print(i, n[0])