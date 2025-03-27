from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about-me')
def about_me():
    return render_template("about_me.html")

@app.route('/about-flask')
def about_flask():
    return render_template("about_flask.html")

if __name__ == '__main__':
    app.run(debug=True)