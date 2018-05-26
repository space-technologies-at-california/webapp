default: clean run

clean:
	rm -f static/data/cache.json

run:
	bash -c "sleep 1; open http://127.0.0.1:5000" &
	python app.py
	
update:
	bash -c "git checkout v1; git add -u; git commit; git push; git checkout master" || git checkout master
	git merge v1 -m "obtain updates from v1 branch"
	git push
	git checkout heroku
	git merge v1 -m "obtain updates from v1 branch"
	git push
	git checkout ocf
	git merge v1 -m "obtain updates from v1 branch"
	git push
	git checkout v1
	ssh ocf-stac-webapp 'cd myapp/src; git checkout -- .; git pull; cd ..; ./restart'

# useage: make json file=<path-to-file>
json:
	python blog.py $(file)

updateBlogContent:
	python markdown/update-blog-content.py $(file)

# make blog-update file=<path-to-file>
blog-update: json updateBlogContent
