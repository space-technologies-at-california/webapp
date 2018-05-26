# Flask Webapp
This is the new flask webapp for STAC as the core landing page, in replacement of the legacy static webapp.

**Always remember to PULL from ocf branch to get the UPDATED database, before you make any changes locally to the database file.**

### Run the app

You need Makefile for this to work.

To run the app, type `make`. This will delete the `static/data/cache.json` file, restart the app, and open the browser for you to see the site

If you don't see any changes you made, either clean your browser cache, or type `make clean` to delete `static/data/cache.json` file saved.

### OCF SSH

To access webapp

```
ssh stac@apphost.ocf.berkeley.edu
```

The repo is under `myapp/src/` linked to the `ocf` branch of the stacweb repo.

To restart the app, run `./restart` under `myapp` folder

To run the app manually, run `./run` under `myapp` folder

### New Login

To create your own admin account online, run the following

```
$ python -i auth_helper.py
$ create_login(<your-username-string-here>, <your-password-string-here>)
```

### Add New Members

To add new members, write a json file for each new member, and save them all as `firstname-lastname.json` under `static/tmp/new_members` folder. 

Save any images under `static/img/team/member` as `firstname-lastname.xxx` with properly cropped image ratio of 1 : 1.4

An example json schema is included in the folder as "example.txt" for your reference. 

Then, run

```
$ python -i add_helper.py
$ add_members("static/tmp/new_members")
```

### Add New Advisors

To add new advisors, write a json file for each new advisor, and save them all as `firstname-lastname.json` under `static/tmp/new_advisors` folder. 

Save any images under 'static/img/team/advisor' as "firstname-lastname.xxx" with properly cropped image ratio of 1 : 1.4

An example json schema is included in the folder as "example.txt" for your reference

Then, run

```
$ python -i add_helper.py
$ add_members("static/tmp/new_advisors")
```

