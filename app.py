from flask import Flask, render_template


app = Flask(__name__, template_folder=".")
print("__name__:", __name__)


@app.route("/")
def hello_world():
    return "<p> Hello user </p>"
    return render_template("welcome.html")
    