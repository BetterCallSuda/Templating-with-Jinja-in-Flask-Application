from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/guess/<name>")
def home(name):
    name = name.title()
    age_url = requests.get(f"https://api.agify.io?name={name.lower()}")
    age_url = age_url.json().get("age")

    gender_url = requests.get(f"https://api.genderize.io?name={name.lower()}")
    gender_url = gender_url.json().get("gender")

    return render_template( 'index.html', person_name = name,
                            person_age = age_url,
                            person_gender = gender_url)


if __name__ == "__main__":
    app.run(debug=True)