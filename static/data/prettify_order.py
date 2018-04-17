import os
import json
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder", type=str)
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

members = glob.glob(args.folder + "/*.json")

old = list(map(lambda x: (x, json.load(open(x))), members))

new = sorted([(x, y) for x, y in old if y["profile-order"] is not None], key=lambda x: x[1]["profile-order"])
new += sorted([(x, y) for x, y in old if y["profile-order"] is None], key=lambda x: x[1]["name"])

for i, n in enumerate(new):
    n[1]["profile-order"] = i + 1
    with open(n[0], "w") as f:
        json.dump(n[1], f, indent=2)

    if args.verbose:
        print(i+1, n[0])
