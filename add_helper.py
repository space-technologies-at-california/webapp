import os
import glob
import json
import datetime
import database
from __init__ import conn, sanitize_input


def add_members(folder):
    if len(folder) <= 0:
        return
    elif folder[-1] == "/":
        folder = folder[:-1]
    member = [json.loads(open(x).read())
              for x in glob.glob("{}/*.json".format(folder))]
    member = {
        x['name'].lower().strip().replace(' ', '-'): x for x in member
    }
    member = sanitize_input(member)

    template = """
        INSERT or REPLACE INTO people VALUES ("{0}", "{1}", "{2}", "{3}", "{4}");
        INSERT or REPLACE INTO members VALUES ("{0}", "{5}", "{6}", {7});
        INSERT or REPLACE INTO links VALUES ("{0}", "{8}", "{9}", "{10}", "{11}", "{12}", '{13}');
        INSERT or REPLACE INTO contacts VALUES ("{0}", "{14}");
    """

    for k, v in member.items():
        try:
            first, last = v['name'].strip().split(" ")
            def escape_null(x): return x if x else "NULL"
            conn.executescript(template.format(
                k, first, last, v["photo"], v["bio"].encode('utf-8'),
                v["major"], v["title"], v["profile-order"],
                v["links"]["github"], v["links"]["linkedin"], v["links"]["twitter"], v["links"]["web"], "NULL", "NULL",
                v["links"]["email"].replace("mailto:", "")).replace('"NULL"', 'null'))
        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break

def add_alumni(folder):
    if len(folder) <= 0:
        return
    elif folder[-1] == "/":
        folder = folder[:-1]
    alumni = [json.loads(open(x).read())
              for x in glob.glob("{}/*.json".format(folder))]
    alumni = {
        x['name'].lower().replace(' ', '-'): x for x in alumni
    }
    alumni = sanitize_input(alumni)

    template = """
        INSERT or REPLACE INTO people VALUES ("{0}", "{1}", "{2}", "{3}", "{4}");
        INSERT or REPLACE INTO alumni VALUES ("{0}", "{5}", "{6}", {7});
        INSERT or REPLACE INTO links VALUES ("{0}", "{8}", "{9}", "{10}", "{11}", "{12}", '{13}');
        INSERT or REPLACE INTO contacts VALUES ("{0}", "{14}");
    """
    for k, v in alumni.items():
        try:
            first, last = v['name'].strip().split(" ")
            def escape_null(x): return x if x else "NULL"
            conn.executescript(template.format(
                k, first, last, v["photo"], v["bio"].encode('utf-8'),
                v["major"], v["title"], v["profile-order"],
                v["links"]["github"], v["links"]["linkedin"], v["links"]["twitter"], v["links"]["web"], "NULL", "NULL",
                v["links"]["email"].replace("mailto:", "")).replace('"NULL"', 'null'))
        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break


def add_advisors(folder):
    if len(folder) <= 0:
        return
    elif folder[-1] == "/":
        folder = folder[:-1]
    advisors = [json.loads(open(x).read())
                for x in glob.glob("{}/*.json".format(folder))]
    advisors = {
        x['name'].lower().replace(' ', '-'): x for x in advisors
    }
    advisors = sanitize_input(advisors)

    template = """
        INSERT or REPLACE INTO people VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
        INSERT or REPLACE INTO advisors VALUES ('{0}', '{5}', {6});
    """

    for k, v in advisors.items():
        try:
            first, last = v['name'].split(" ")
            def escape_null(x): return x if x else "NULL"
            conn.executescript(template.format(
                k, first, last, v["photo"], v["bio"].encode('utf-8'),
                v["affiliation"], v["profile-order"]).replace('"NULL"', 'null'))
        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break


def update_advisors(folder):
    if len(folder) <= 0:
        return
    elif folder[-1] == "/":
        folder = folder[:-1]
    advisors = [json.loads(open(x).read())
                for x in glob.glob("{}/*.json".format(folder))]
    advisors = {
        x['name'].lower().replace(' ', '-'): x for x in advisors
    }
    advisors = sanitize_input(advisors)

    template = """
        UPDATE people set first_name='{1}', last_name='{2}', photo='{3}', bio='{4}') where id='{0}';
        UPDATE advisors set affiliation='{5}', profile_order={6} where id='{0}';
    """

    for k, v in advisors.items():
        try:
            first, last = v['name'].split(" ")
            def escape_null(x): return x if x else "NULL"
            conn.executescript(template.format(
                k, first, last, v["photo"], v["bio"].encode('utf-8'),
                v["affiliation"], v["profile-order"]).replace('"NULL"', 'null'))
        except Exception as e:
            print("failed at", k, "for", e, "\n v:\n", v)
            break
