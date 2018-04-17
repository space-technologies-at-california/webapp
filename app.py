import os
import database
import blog
import json
from flask import request
from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from config import config
from collections import OrderedDict

app = Flask(__name__)

real_root_path = os.path.dirname(os.path.realpath(__file__)) + "/"

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
	# return render_template("join.html")
	return redirect("https://goo.gl/forms/s86BFh1eUmHFRM0P2")

@app.route("/admin-update/member_id=<member_id>", methods=['GET', 'POST'])
def admin_update_member(member_id):

    if request.method == 'GET':

        p = database.fetchone("""
            SELECT  a.first_name || " " || a.last_name as name,
                    a.first_name as first_name,
                    a.last_name as last_name,
                    a.photo as photo,
                    b.major as major,
                    b.title as title,
                    a.bio as bio,
                    c.github as github,
                    c.linkedin as linkedin,
                    c.twitter as twitter,
                    c.web as web,
                    d.email as email
            FROM people as a, members as b, links as c, contacts as d
            WHERE a.id = b.id AND a.id = c.id And a.id = d.id AND b.id = '{0}'
            ORDER BY profile_order
        """.format(member_id))

        fail = p is None
        info = {}

        if not fail:
            info = OrderedDict({
                "name": p[0],
                "first_name": p[1],
                "last_name": p[2],
                "photo": p[3],
                "major": p[4],
                "title": p[5],
                "bio": p[6],
                "github": p[7],
                "linkedin": p[8],
                "twitter": p[9],
                "web": p[10],
                "email": p[11]
            })

        return render_template("admin-update-members.html", member=member_id, fail=fail, info=info)

    else:
        escape_input = lambda x: "NULL" if x is None or x.lower().strip() == "none" or x.lower().strip() == "null" else database.escape(x.strip())


        database.execute("""
            UPDATE people set first_name='{}', last_name='{}', photo='{}', bio='{}' WHERE id = '{}';
        """.format(escape_input(request.form["first_name"]), escape_input(request.form["last_name"]), escape_input(request.form["photo"]), escape_input(request.form["bio"]), escape_input(member_id)).replace("'NULL'", 'null'))

        database.execute("""
            UPDATE members set major='{}', title='{}' WHERE id = '{}';
        """.format(escape_input(request.form["major"]), escape_input(request.form["title"]), escape_input(member_id)).replace("'NULL'", 'null'))

        database.execute("""
            UPDATE links set github='{}', linkedin='{}', twitter='{}', web='{}' WHERE id = '{}';
        """.format(escape_input(request.form["github"]), escape_input(request.form["linkedin"]), escape_input(request.form["twitter"]), escape_input(request.form["web"]), escape_input(member_id)).replace("'NULL'", 'null'))

        database.execute("""
            UPDATE contacts set email='{}' WHERE id = '{}';
        """.format(escape_input(request.form["email"]), escape_input(member_id)).replace("'NULL'", 'null'))

    return redirect(url_for("team"))

##################### About Us Pages #####################

@app.route("/aboutus")
def aboutus():
	return render_template("summary-page.html", config=config["aboutus"])

@app.route("/team")
@app.route("/aboutus/team")
def team():

    everyone = database.fetchall("""
        SELECT  a.first_name || " " || a.last_name as name,
                a.photo as photo,
                b.major as major,
                b.title as title,
                a.bio as bio,
                c.github as github,
                c.linkedin as linkedin,
                c.twitter as twitter,
                c.web as web,
                d.email as email
        FROM people as a, members as b, links as c, contacts as d
        WHERE a.id = b.id AND a.id = c.id And a.id = d.id
        ORDER BY profile_order
    """)
    
    members = list()
    for p in everyone:
        members.append({
            "name": p[0],
            "photo": p[1],
            "major": p[2],
            "title": p[3],
            "bio": p[4],
            "links": {
                "github": p[5],
                "linkedin": p[6],
                "twitter": p[7],
                "web": p[8],
                "email": "mailto:" + p[9] if p[9] else p[9]
            }
    })   

    return render_template("team.html", config=config["team"], members=members)

@app.route("/industry-advisor")
@app.route("/industry-advisors")
@app.route("/aboutus/industry-advisor")
@app.route("/aboutus/industry-advisors")
def industry_advisors():

    everyone = database.fetchall("""
        SELECT  a.first_name || " " || a.last_name as name,
                a.photo as photo,
                b.affiliation as affiliation,
                a.bio as bio
        FROM people as a, advisors as b
        WHERE a.id = b.id
        ORDER BY b.profile_order
    """)
    
    advisors = list()
    for p in everyone:
        advisors.append({
            "name": p[0],
            "photo": p[1],
            "affiliation": p[2],
            "bio": p[3].split("\n")
        }) 
    
    return render_template("industry-advisors.html", config=config["industry-advisors"], advisors=advisors)

##################### Project Pages #####################

@app.route("/project")
@app.route("/projects")
@app.route("/project/<name>")
@app.route("/projects/<name>")
def project(name="example"):

    project_data = database.fetchone("""
        SELECT  a.page_title as title,
                a.page_banner_img as background,
                a.blog_img_alt as post_img_alt,
                a.blog_img as post_img_url,
                a.blog_date as blog_date,
                a.blog_title as blog_title,
                b.project_lead as project_lead,
                b.project_lead_icon as project_lead_icon,
                a.blog_tag as blog_tag,
                a.blog_tag_icon as blog_tag_icon,
                a.blog_content_markdown as blog_content_markdown
        FROM blog_posts as a, projects as b
        WHERE a.project_id = b.id AND a.project_id = '{0}'
    """.format(name))


    projects = {
      "title": project_data[0],
      "background": project_data[1],
      "post-img": {
        "alt": project_data[2],
        "url": project_data[3]
      },
      "date": project_data[4],
      "blog-title": project_data[5],
      "blog-info": {
        "Project Led by": {
          "list": project_data[6].split("\n"),
          "icon": project_data[7]
        },
        "Tagged as": {
          "list": project_data[8].split("\n"),
          "icon": project_data[9]
        }
      },
      "blog-content": json.loads(blog.create_json(real_root_path + project_data[10], returnString=True))["blog-content"]
    }

    return render_template("project.html", projects=projects)

##################### Sponsor Pages #####################

@app.route("/sponsor")
def sponsor():
	return render_template("summary-page.html", config=config["sponsor"])

@app.route("/sponsor/industry-partnership")
@app.route("/industry-partnership")
def industry_partnership():
	return render_template("industry-partnership.html", config=config["industry-partnership"])


@app.route("/sponsor/confirmation")
@app.route("/industry-partnership/confirmation")
@app.route("/sponsor/industry-partnership/confirmation")
def sponsor_confirmation():
	return render_template("sponsor-confirmation.html", config=config['sponsor-confirmation'])

##################### Additional Pages #####################

@app.route("/sts")
def sts():
    return render_template("stac-sts.html")

@app.route("/kickstarter")
def kickstarter():
    return render_template("kickstarter.html", config=config["kickstarter"])

##################### Error Handling #####################

@app.route('/404')
def error_page():
	return render_template('404.html')

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/404")

@app.errorhandler(500)
def internal_server_error(e):
    return redirect("/404")

#################### Main App #####################
if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.debug = True

