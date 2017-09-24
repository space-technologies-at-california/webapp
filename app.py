import os
import json
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask(__name__)

def load_json(path, root="static/data/", project=False):
	if project:
		root += 'projects/'
	return json.loads(open(root + path).read())

# Cache configuration files
config = {
	"navbar": load_json("navbar.json"),
	"about-us": load_json("about-us.json"),
	"home" : load_json("home-configuration.json"),
	"project": {
		"example": load_json("example.json", project=True),
	}
}

@app.context_processor
def utility_processor():
    return dict(navbar=config["navbar"], aboutus=config['about-us'])

##################### Pages #####################
@app.route("/")
@app.route("/home")
def index():
	return render_template("home.html", config=config['home'])

@app.route("/join")
@app.route("/apply")
def join():
	return render_template("join.html")

@app.route("/project")
@app.route("/projects")
@app.route("/project/<name>")
@app.route("/projects/<name>")
def project(name="example"):
	return render_template("project.html", config=config['project'][name])


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

