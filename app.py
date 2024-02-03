from flask import Flask, render_template, url_for

app = Flask(__name__)

skills = {
    "python": 90,
    "Go Lang": 60,
    "C": 40,
    "CSS": 50,
    "HTML": 92,
    "JavaScript": 74,
    "SQL": 80,
}


@app.route("/")
def home():
    return render_template("home.html", skills=skills)


@app.template_filter("CSC")
def classify_skill_color(per: int) -> str:
    if per < 30:
        return "danger"
    elif per < 50:
        return "warning"
    elif per < 80:
        return "info"
    else:
        return "success"


if __name__ == "__main__":
    app.run(debug=True)
