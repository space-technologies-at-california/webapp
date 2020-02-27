import os
import glob
import json
import datetime

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
		"industry-advisors": load_json("industry-advisors.json"),
		"aboutus": load_json("aboutus.json"),
		"team": load_json("team.json"),
		"alumni": load_json("alumni.json"),
		"sponsor": load_json("sponsor.json"),
		"industry-partnership": load_json("industry-partnership.json"),
		"sponsor-confirmation": load_json("sponsor-confirmation.json"),
		"icon": load_json("icon.json"),
		"kickstarter": load_json("kickstarter.json"),
		"projectDescription": load_json("projectDescription.json"),
		"fundraising": load_json("fundraising.json")
	}

	with open(real_root_path + "static/version.txt", "r") as f:
		cur_version_number = float(f.read().strip())
	cur_version_number = round(cur_version_number + 0.1, 1)
	with open(real_root_path + "static/version.txt", "w") as f:
		f.write(str(cur_version_number))
	config["version"] = cur_version_number


	# Cache configuration for Sponsor
	config["industry-partnership"].update({
		"partner-logo": { x.split(".")[0][x.index("img"):] : x[x.index("img"):] for x in glob.glob(real_root_path + "static/img/logo/partner/*")}
	})

	# Update Rights Info with current year
	config["club"]["rights"] = config["club"]["rights"].format(datetime.datetime.now().year)

	# Save cache
	with open("static/data/cache.json", "w") as f:
		f.write(json.dumps(config, indent=2))
