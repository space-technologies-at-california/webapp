# Flask Webapp
This is the new flask webapp for STAC as the core landing page, in replacement of the legacy static webapp.

### Run the app

You need Makefile for this to work (in order to run 'make')

You also need to download Flask, https://pypi.org/project/Flask/.

Type in bash: 'virtualenv flask' then 'cd flask'

Then, type 'source bin/activate' 

Back out of the flask directory by typing 'cd ..'

To run the app, type `make`. This will delete the `static/data/cache.json` file, restart the app, and open the browser for you to see the site

If you don't see any changes you made, either clean your browser cache, or type `make clean` to delete `static/data/cache.json` file saved.

After running `make`, you can refresh the page to see live changes (don't need to run `make` again).

### Update Website

**First, always remember to PULL from ocf branch to get and merge the UPDATED database, before you make any changes locally to the database file, in case someone has updated information through web online portal.**

***As of February 2022, master is the most updated and is to be used instead of ocf branch***


Then, for new updates and features, always work a seaprate branch when making changes. For example, use the `development` branch. 

Type `make` to update the cache and to view changes locally to make sure everthing works.

Then, merge and push your changes to both `master` branch and `ocf` branch. 


### OCF SSH

To access webapp on OCF to upload/update the site.

```
ssh stac@vampires.ocf.berkeley.edu
```

Password can be found in drive. The repo is under `myapp/src/` linked to the `ocf` branch of the stacweb repo. 

Git status to check status.

Git pull origin master to pull most updated code.

To restart the app, run `./restart` under `myapp` folder (cd ../ from src)

To run the app manually, run `./run` under `myapp` folder.

***Editor's note: use both ./restart then ./run ***


### Members

#### Update Existing Members

Go to `stac.berkeley.edu/admin` and login using your account.

You can make live changes to members there, except the photos. See below for details on how to create an admin account.

#### Add New Members/Update Members via Code

To add new members, write a json file for each new member, and save them all as `firstname-lastname.json` under `static/data/member` folder. 

Save any images under `static/img/team/member` as `firstname-lastname.xxx` with properly cropped image ratio of 1 : 1.4. Crop images in Figma, see STAC figma file.

An example json schema is included in the folder as "example.txt" for your reference. 

Then, run

```
$ python -i add_helper.py
$ add_members("static/data/member")
```

This will update, replace, or create database entries for everything in "static/data/member".

### Advisors (has not been updated since 2020. To be edited and mofified)

#### Update Existing Advisors


To update existing advisors, write a updated json file for each to-be-updated advisor, and save them all as `firstname-lastname.json` under `static/tmp/update_advisors` folder. 

Save any images under 'static/img/team/advisor' as "firstname-lastname.xxx" with properly cropped image ratio of 1 : 1.4

An example json schema is included in the folder as "example.txt" for your reference. Some of the json files for existing advisors are saved under `static/data/industry-advisors` folders.

Then, run

```
$ python -i add_helper.py
$ update_advisors("static/tmp/update_advisors")
```

Once you finish updating the advisors, replace any old json files for the advisors under the `static/data/industry-advisors` folders with your new json files, for future updates references.


#### Add New Advisors

To add new advisors, write a json file for each new advisor, and save them all as `firstname-lastname.json` under `static/tmp/new_advisors` folder. 

Save any images under 'static/img/team/advisor' as "firstname-lastname.xxx" with properly cropped image ratio of 1 : 1.4

An example json schema is included in the folder as "example.txt" for your reference

Then, run

```
$ python -i add_helper.py
$ add_members("static/tmp/new_advisors")
```

Once you finish adding the advisors, move your json files out of the `static/tmp/new_advisors` folder, and place them into the `static/data/industry-advisors` folder, for future updates references.



**Shortcut - Not working February 2022**

For ease of updating website, you have the option to set it up so you can use `make` commands to do everyhing for you.

First, put your public key on the ocf server so you don't need to type password when sshing.

Second, add the following line to your `.ssh/config` file

```
Host ocf-stac-webapp
HostName apphost.ocf.berkeley.edu
User stac
```

Now, to sync changes under `development` branch to both `ocf` and `master` branch, type

```
make update
```

To restart the website in ocf remote server, type

```
make restart-remote
```


### New Login

To create your own admin account online, run the following

```
$ python -i auth_helper.py
$ create_login(<your-username-string-here>, <your-password-string-here>)
```


