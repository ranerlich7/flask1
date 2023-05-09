from flask import Flask, render_template
from news import news_bp

app = Flask(__name__)
app.register_blueprint(news_bp)

@app.route("/")
def hello_world():
    print("hello")
    return "<p>Hello, World!</p><button>Press</button>"

@app.route("/sport")
def sport():
    return render_template("sports.html")
    # return "<p>This is the SPORT section</p>"

if __name__ == '__main__':
    app.run(debug=True, port=9000)
