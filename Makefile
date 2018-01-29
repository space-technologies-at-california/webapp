default: clean run

clean: static/data/cache.json
	rm -f static/data/cache.json

run:
	open http://127.0.0.1:5000/
	python app.py
	
update:
	bash -c "git checkout v1; git add -A; git commit; git push;" || git checkout master
	git merge v1
	git push
	git checkout heroku
	git merge v1
	git push
	git checkout ocf
	git merge v1
	git push
	git checkout v1
	ssh ocf-stac-webapp 'cd myapp/src; git pull; cd ..; ./restart'
