import sqlite3
import os
import json
import glob

#########################
# CREATE NEW DATABASE
#########################

DATABASE_FILE = 'db'
# DATABASE_FILE = ':memory:'
if DATABASE_FILE in os.listdir('.'):
    os.remove(DATABASE_FILE)
conn = sqlite3.connect(DATABASE_FILE)


#########################
# SQL AND HTML ESCAPE
#########################

def make_escaper(replacements):
    def escaper(inp):
        for old, new in replacements.items():
            inp = inp.replace(old, new)
        return inp
    return escaper

escape_sql = make_escaper({
    ';': '\;',
    "'": "\'",
    '--': '&ndash;',
    '*': '&#42;',
    })

escape_html = make_escaper({
    '<': '&lt;',
    '>': '&gt;'
    })


#########################
# TABLE DEFINITIONS
#########################

conn.executescript("""
    CREATE TABLE people (
        id text PRIMARY KEY UNIQUE NOT NULL, 
        first_name text NOT NULL, 
        last_name text NOT NULL, 
        photo text NOT NULL, 
        bio text NOT NULL);

    CREATE TABLE members (
        id text UNIQUE NOT NULL,
        major text NOT NULL, 
        title text NOT NULL,
        profile_order decimal);

    CREATE TABLE advisors (
        id text PRIMARY KEY UNIQUE NOT NULL,
        affiliation text NOT NULL, 
        profile_order decimal);

    CREATE TABLE links (
        id text PRIMARY KEY UNIQUE NOT NULL, 
        github text, 
        linkedin text, 
        twitter text, 
        web text);

    CREATE TABLE contacts (
        id text PRIMARY KEY UNIQUE NOT NULL, 
        email text);

    CREATE TABLE blog_posts (
        id text PRIMARY KEY UNIQUE NOT NULL, 
        page_title text NOT NULL,
        page_banner_img text,
        blog_title text NOT NULL,
        blog_img text NOT NULL,
        blog_img_alt text,
        blog_date text NOT NULL,
        blog_tag text,
        blog_tag_icon text,
        blog_content_markdown text NOT NULL,
        project_id text);

    CREATE TABLE projects (
        id text PRIMARY KEY UNIQUE NOT NULL, 
        full_name text NOT NULL,
        project_lead text,
        project_lead_icon text,
        project_type text);

    CREATE TABLE icons (
        name text PRIMARY KEY UNIQUE NOT NULL, 
        font_awesome text NOT NULL,
        themify text NOT NULL);

""")

#########################
# SQL QUERY FORMATTER
#########################

def sanitize_input(dictionary):
    for k, v in dictionary.items():
        if v is None: 
            v = "NULL"
        elif type(v) is float or type(v) is int:
            continue
        elif type(v) is list:
            v = "\n".join(v).strip()
        elif type(v) is dict:
            v = sanitize_input(v)
            continue
        elif type(v) is str:
            v = v.strip()
            if len(v) == 0:
                v = "NULL"
        dictionary[k] = escape_html(escape_sql(v))
    return dictionary

#########################
# MEMBER INITIALIZATION
#########################

def initialize_member():
    member = [json.loads(open(x).read()) for x in glob.glob("static/data/member/*.json")]
    member = {
        x['name'].lower().strip().replace(' ', '-'): x for x in member
    }
    member = sanitize_input(member)

    template = """
        INSERT INTO people VALUES ("{0}", "{1}", "{2}", "{3}", "{4}");
        INSERT INTO members VALUES ("{0}", "{5}", "{6}", {7});
        INSERT INTO links VALUES ("{0}", "{8}", "{9}", "{10}", "{11}");
        INSERT INTO contacts VALUES ("{0}", "{12}");
    """

    for k, v in member.items():
        try:
            first, last = v['name'].strip().split(" ")
            escape_null = lambda x: x if x else "NULL"
            conn.executescript(template.format(\
                k, first, last, v["photo"], v["bio"], \
                    v["major"], v["title"], v["profile-order"],\
                    v["links"]["github"], v["links"]["linkedin"], v["links"]["twitter"], v["links"]["web"], \
                    v["links"]["email"]).replace('"NULL"', 'null'));
        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break

initialize_member()

#########################
# ADVISOR INITIALIZATION
#########################

def initialize_advisor():
    advisors = [json.loads(open(x).read()) for x in glob.glob("static/data/industry-advisors/*.json")]
    advisors = {
        x['name'].lower().replace(' ', '-'): x for x in advisors
    }
    advisors = sanitize_input(advisors)

    template = """
        INSERT INTO people VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
        INSERT INTO advisors VALUES ('{0}', '{5}', {6});
    """

    for k, v in advisors.items():
        try:
            first, last = v['name'].split(" ")
            escape_null = lambda x: x if x else "NULL"
            conn.executescript(template.format(\
                k, first, last, v["photo"], v["bio"], \
                    v["affiliation"], v["profile-order"]).replace('"NULL"', 'null'));
        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break

initialize_advisor()

#############################
# PROJECT BLOG INITIALIZATION
#############################

def initialize_project_blog():
    projects = {
        x.split("/")[-1].replace(".json", ""): json.loads(open(x).read()) for x in glob.glob("static/data/projects/*.json")
    }

    template = """
        INSERT INTO blog_posts VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');
        INSERT INTO projects VALUES ('{}', '{}', '{}', '{}', '{}');
    """

    for k, v in projects.items():
        try:
            tmp = { 
                "id": k,
                "page_title": v["title"],
                "page_banner_img": v["background"],
                "blog_title": v["blog-title"],
                "blog_img": v["post-img"]["url"],
                "blog_img_alt": v["post-img"]["alt"],
                "blog_date": v["date"],
                "blog_tag": "\n".join(v["blog-info"]["Tagged as"]["list"]),
                "blog_tag_icon": v["blog-info"]["Tagged as"]["icon"],
                "blog_content_markdown": "markdown/{}.md".format(k),
                "project_id": k,
            }
            tmp = sanitize_input(tmp)

            tmp2 = {
                "id": k,
                "full_name": v["title"],
                "project_lead": "\n".join(v["blog-info"]["Project Led by"]["list"]),
                "project_lead_icon": v["blog-info"]["Project Led by"]["icon"],
                "project_type": ", ".join(v["blog-info"]["Tagged as"]["list"]),
            }
            tmp2 = sanitize_input(tmp2)

            conn.executescript(template.format(tmp["id"], tmp["page_title"], tmp["page_banner_img"], tmp["blog_title"], tmp["blog_img"], tmp["blog_img_alt"], tmp["blog_date"], tmp["blog_tag"], tmp["blog_tag_icon"], tmp["blog_content_markdown"], tmp["project_id"], tmp2["id"], tmp2["full_name"], tmp2["project_lead"], tmp2["project_lead_icon"], tmp2["project_type"]).replace('"NULL"', 'null'))

        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break

initialize_project_blog()

#############################
# ICON INITIALIZATION
#############################

def initialize_icons():
    icons = sanitize_input(json.load(open("static/data/icon.json")))

    template = """
        INSERT INTO icons VALUES ('{0}', '{1}', '{2}');
    """

    for k, v in icons.items():
        try:
            conn.executescript(template.format(k, v["fa"], v["ti"]).replace('"NULL"', 'null'));
        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break

initialize_icons()


#########################
# COMMIT CHANGES
#########################

conn.commit()
