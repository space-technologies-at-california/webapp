import os
import glob
import json
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)
cache = SimpleCache()

def load_json(path, root="static/data/", subroot=""):
	root += subroot
	return json.loads(open(root + path).read())

if "cache.json" in os.listdir("."):
	config = load_json("cache.json")
	print("cache loaded...")
else:
	# Cache configuration files
	config = {
		"navbar": load_json("navbar.json"),
		"club": load_json("club.json"),
		"home" : load_json("home-configuration.json"),
		"project": { x.split("/")[-1].split(".")[0]  : load_json(x, root="", subroot="") for x in glob.glob("static/data/projects/*.json") },
		"team": load_json("team.json"),
		"sponsor": load_json("sponsor.json"),
		"sponsor-confirmation": load_json("sponsor-confirmation.json"),
		"icon": load_json("icon.json")
	}

	# Cache configuration files II
	config["team"].update({
		"member": [ load_json(x, root="", subroot="") for x in glob.glob("static/data/member/*.json")]
	})
	config['team']['member'].sort(key=lambda x: x['profile-order'] if x['profile-order'] is not None else float('inf')) # sort profile order
	config["sponsor"].update({
		"partner-logo": { x.split(".")[0] : x for x in glob.glob("static/img/logo/partner/*")}
	})
	# save cache
	with open("static/data/cache.json", "w") as f:
		f.write(json.dumps(config, indent=2))



##################### Cross Page Functionalities #####################

@app.context_processor
def utility_processor():
    return dict(navbar=config["navbar"], club=config['club'], icon=config["icon"])

##################### Pages #####################
@app.route("/")
@app.route("/home")
def index():
	return render_template("home.html", config=config['home'])

@app.route("/join")
@app.route("/apply")
def join():
	return render_template("join.html")

@app.route("/sponsor/confirmation")
def sponsor_confirmation():
	return render_template("sponsor-confirmation.html", config=config['sponsor-confirmation'])

@app.route("/project")
@app.route("/projects")
@app.route("/project/<name>")
@app.route("/projects/<name>")
def project(name="example"):
	return render_template("project.html", config=config['project'][name])

@app.route("/team")
@app.route("/aboutus/team")
def team():
	return render_template("team.html", config=config["team"])

@app.route("/sponsor")
def sponsor():
	return render_template("sponsor.html", config=config["sponsor"])

##################### Error Handling #####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

#################### Main App #####################
if __name__ == "__main__":
    #app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True

