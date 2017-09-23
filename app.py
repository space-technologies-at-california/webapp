import os
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

# @app.context_processor
# def utility_processor():
#     return dict(globalVariableName=variable)

@app.route("/")
@app.route("/home")
def index():
    # return render_template("main-page.html")
    return "Hello World"


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

