from flask import Flask, render_template, request, redirect, url_for

# . -> current dir
# .. -> parent dir

app = Flask(__name__)
print("__name__:", __name__)


@app.route("/")
def hello_world():
    return render_template("welcome.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form ["username"]
        passcode = request.form ["password"]
        if username == "root" and passcode == "groot":
            
            print("url_for('hello_world'):{}".format(url_for('hello_world')))
            print("url_for('login'):{}".format(url_for('login')))
            print("url_for('register'):{}".format(url_for('register')))

            hello_world_endpoint = url_for('hello_world')
            return redirect(hello_world_endpoint)

            # redirect:
            # it takes an endpoint as input
            # redirects user to that endpoint

            # url_for: 
            # takes a function name as input
            # returns an endpoint
        else:
            return "Invalid username or password. Can't login."
            # TODO: 
            # send a msg: Invalid username or password. Can't login.
            # he should still be in login page
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

@app.route("/user")
def user():
    print(request.args)
    return request.form
    