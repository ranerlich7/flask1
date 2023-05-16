from flask import Flask, render_template, request, redirect
from news import news_bp

app = Flask(__name__)
app.register_blueprint(news_bp)

@app.route("/", methods=['GET','POST'])
def index():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "ran" and password == "123":
        return redirect("/news")
    print(f" ***** {username}-{password}")
    return render_template("index.html")

@app.route("/sport")
def sport():
    return render_template("sports.html")
    # return "<p>This is the SPORT section</p>"

if __name__ == '__main__':
    app.run(debug=True, port=9000)


"""
ex1:
1. create a new screen - index.html
2. form with fields: username, password (input fields, form should have method POST)
3. get parameters in python using request.form.get("username")...
4. check if user=yourname pass=your password then write "WELCOME" or redirect to news.html
 if not return to login screen

 ex2:
 make a new screen - the user inputs 2 numbers x,y and get the result of x*y
 """