from flask import Flask, redirect, request, url_for , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("dash.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Resume")
def resume():
    return render_template("resume.html")


if __name__ == "__main__":
    app.run(debug=True)

