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

project = {
    "title": "project1",
    "img_path": "imgs/photo-1572177812156-58036aae439c",
    "desc": "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
    "details": "#",
    "project_url": "#",
    "github_url": "#",
}

projects = [project for _ in range(4)]


@app.route("/")
def home():
    return render_template("home.html", skills=skills, projects=projects)


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
