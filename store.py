from flask import Flask, render_template

store = Flask(__name__)

@store.route("/")
def index():
    return render_template("index.html")


if __name__=="__main__":
    store.jinja_env.auto_reload = True
    store.run(debug=True)

