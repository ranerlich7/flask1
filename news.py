from flask import Blueprint, render_template
news_bp = Blueprint('news', __name__,url_prefix='/news')

@news_bp.route('/')
def news():
    return render_template("news.html")
    # <p> **** This is the NEWS ****</p>"

@news_bp.route('/global')
def news_global():
    return "<p> **** This is the GLOBAL NEWS ****</p>"



