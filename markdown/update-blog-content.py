import json
import argparse


def update(path):
    if ".json" not in path and ".md" in path:
        path = path.replace(".md", ".json")
    else:
        print("incorrect path, needs to be .json or .md", path)
        return
    filename = path.split("/")[-1]
    newContent = json.load(open(path, "r"))
    oldContent = json.load(open("static/data/projects/{0}".format(filename), "r"))
    oldContent["blog-content"] = newContent["blog-content"]
    with open("static/data/projects/{0}".format(filename), "w") as f:
        json.dump(oldContent, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="a parser that updates the blog content of the project file based on a json")
    parser.add_argument("source", type=str, help="<path-to-file.md>.json")
    args = parser.parse_args()

    try:
        update(args.source)
        print("blog content updated: {0}".format(args.source))
        print("SUCCESS")
    except Exception as e:
        print("FAILED\n")
        print(e)

