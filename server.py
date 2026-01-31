from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/blog")
def blog():
    blog_url = requests.get("https://api.npoint.io/df8ecc891de9421d14f5")
    blogs = blog_url.json()
    return render_template("index.html", post = blogs)

if __name__ == "__main__":
    app.run(debug=True)

