import os
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

##################### Core Pages #####################
@app.route("/")
@app.route("/home")
def index():
	return render_template("home.html", config=config['home'], sponsor=config["industry-partnership"])

@app.route("/join")
@app.route("/apply")
def join():
	return render_template("join.html")

##################### About Us Pages #####################

@app.route("/aboutus")
def aboutus():
	return render_template("summary-page.html", config=config["aboutus"])

@app.route("/team")
@app.route("/aboutus/team")
def team():
	return render_template("team.html", config=config["team"])

@app.route("/industry-advisor")
@app.route("/industry-advisors")
@app.route("/aboutus/industry-advisor")
@app.route("/aboutus/industry-advisors")
def industry_advisors():
	return render_template("industry-advisors.html", config=config["industry-advisors"])

##################### Project Pages #####################

@app.route("/project")
@app.route("/projects")
@app.route("/project/<name>")
@app.route("/projects/<name>")
def project(name="example"):
	return render_template("project.html", config=config['project'][name])


##################### Sponsor Pages #####################

@app.route("/sponsor")
def sponsor():
	return render_template("summary-page.html", config=config["sponsor"])

@app.route("/sponsor/industry-partnership")
@app.route("/industry-partnership")
def industry_partnership():
	return render_template("industry-partnership.html", config=config["industry-partnership"])


@app.route("/sponsor/confirmation")
def sponsor_confirmation():
	return render_template("sponsor-confirmation.html", config=config['sponsor-confirmation'])


##################### Error Handling #####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

#################### Main App #####################
if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True

