from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from config import config

app = Flask(__name__)


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

@app.route("/advisor")
@app.route("/aboutus/advisor")
def advisor():
	return render_template("advisor.html", config=config["advisor"])

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
    app.run()
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    # app.debug = True

