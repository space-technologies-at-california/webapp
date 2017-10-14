import os
import glob
import json

real_root_path = os.path.dirname(os.path.realpath(__file__)) + "/"

def load_json(path, root="static/data/", subroot=""):
	if real_root_path not in path:
		root = real_root_path + root
	root += subroot
	return json.loads(open(root + path).read())

if "cache.json" in os.listdir(real_root_path + "static/data"):
	config = load_json("cache.json")
	print("cache loaded...")
else:
	# Cache configuration files
	config = {
		"navbar": load_json("navbar.json"),
		"club": load_json("club.json"),
		"home" : load_json("home-configuration.json"),
		"project": { x.split("/")[-1].split(".")[0]  : load_json(x, root="", subroot="") for x in glob.glob(real_root_path + "static/data/projects/*.json") },
		"advisor": load_json("advisor.json"),
		"team": load_json("team.json"),
		"sponsor": load_json("sponsor.json"),
		"sponsor-confirmation": load_json("sponsor-confirmation.json"),
		"icon": load_json("icon.json")
	}

	# Cache configuration for Team
	config["team"].update({
		"member": [ load_json(x, root="", subroot="") for x in glob.glob(real_root_path + "static/data/member/*.json")]
	})
	# sort profile order
	config['team']['member'] = sorted([x for x in config['team']['member'] if x["profile-order"] is not None], key=lambda x: x["profile-order"]) + sorted([x for x in config['team']['member'] if x["profile-order"] is None], key=lambda x: x["name"])

	# Cache configuration for Advisor
	config["advisor"].update({
		"advisor": [ load_json(x, root="", subroot="") for x in glob.glob(real_root_path + "static/data/advisor/*.json")]
	})
	# sort profile order
	config['advisor']['advisor'] = sorted([x for x in config['advisor']['advisor'] if x["profile-order"] is not None], key=lambda x: x["profile-order"]) + sorted([x for x in config['advisor']['advisor'] if x["profile-order"] is None], key=lambda x: x["name"])

	# Cache configuration for Sponsor
	config["sponsor"].update({
		"partner-logo": { x.split(".")[0] : x for x in glob.glob(real_root_path + "static/img/logo/partner/*")}
	})

	# Save cache
	with open("static/data/cache.json", "w") as f:
		f.write(json.dumps(config, indent=2))
