import os
import json
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask(__name__)

def load_json(path, root="static/data/"):
	return json.loads(open(root + path).read())

# Cache configuration files
config = {
	"navbar": load_json("navbar.json"),
	"about-us": load_json("about-us.json"),
	"home" : load_json("home-configuration.json")
}

@app.context_processor
def utility_processor():
    return dict(navbar=config["navbar"], aboutus=config['about-us'])

##################### Pages #####################
@app.route("/")
@app.route("/home")
def index():
	return render_template("home.html", config=config['home'])

@app.route("/demo")
def demo():
	root = "static/img/logo/partner"
	pics = ["{0}/{1}".format(root, x) for x in os.listdir(root)]
	print(pics)
	return render_template("demo.html", pic=pics)

@app.route("/join")
@app.route("/apply")
def join():
	return render_template("join.html")


##################### Error Handling #####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

#################### Main App #####################
if __name__ == "__main__":
    app.run()

