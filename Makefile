default: clean run

clean:
	rm -f static/data/cache.json

run:
	bash -c "sleep 1; open http://127.0.0.1:5000" &
	python app.py
	
update:
	bash -c "git checkout development; git add -u; git commit; git push; git checkout master" || git checkout master
	git merge development -m "obtain updates from development branch"
	git push
	git checkout ocf
	git merge development -m "obtain updates from development branch"
	git push
	git checkout development


# useage: make json file=<path-to-file>
json:
	python blog.py $(file)

updateBlogContent:
	python markdown/update-blog-content.py $(file)

# make blog-update file=<path-to-file>
blog-update: json updateBlogContent


restart-remote:
	# you need to configure a shortcut in .ssh/config to point ocf-stac-webapp
	# to ssh stac@apphost.ocf.berkeley.edu for this to work
	ssh ocf-stac-webapp 'cd myapp/src; git checkout -- .; git pull; cd ..; ./restart'