from flask import Flask, render_template, request 

# . -> current dir
# .. -> parent dir

app = Flask(__name__)
print("__name__:", __name__)


@app.route("/")
def hello_world():
    return render_template("welcome.html")

@app.route("/login")
def login():
    # username: root
    # password: groot

    # redirect
    # return render_template("welcome.html")

    return render_template("Login.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        return "Congrats {}, you have registered successfully".format(username)

    return render_template("Register.html")
