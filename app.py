from flask import (
    Flask,
    jsonify,
    render_template,
    render_template_string,
    request,
    url_for,
)
from base64 import b64encode, b64decode
from asserts import Asserts, projects_data
from models import Certificate, Coding_Platform, Message, Project, Skill, db, FAQs

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

asserts = Asserts()


@app.route("/")
def home():
    # print(data)
    # cps = [
    #     ["CodeWars", "https://www.codewars.com/users/Kibuule%20Noah%20"],
    #     ["Kaggle", "https://www.kaggle.com/tristarnoah"],
    #     ["SoloLearn", "https://www.sololearn.com/en/profile/30214633"],
    # ]
    # for name, link in cps:
    #     cp = Coding_Platform(name, link)
    #     db.session.add(cp)
    # db.session.commit()

    certificates = asserts.certificates
    display_certs = certificates[:4]
    hidden_certs = certificates[4:]
    return render_template(
        "home.html",
        skills=asserts.skills,
        display_certs=display_certs,
        hidden_certs=hidden_certs,
        coding_ps=asserts.coding_platforms,
        projects=welcome_projects(),
    )


@app.route("/projects")
def projects_():
    return render_template("projects.html", projects=asserts.projects)


@app.route("/faqs")
def faqs():
    return render_template("faqs.html", qns=asserts.faqs)


@app.route("/aboutme")
def about_me():
    return render_template("aboutme.html")


@app.route("/contact-me", methods=["POST"])
def contact_me():
    data = request.json
    if data:
        name, email, message = data.values()
        msg = Message(name, email, message)
        db.session.add(msg)
        db.session.commit()
    return jsonify({})


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


@app.template_filter("join_faqs")
def join_faqs(question: str) -> str:
    return question.replace(" ", "-")[:-1]


@app.template_filter("convert_to_base64")
def convert_to_base64(data):
    """
    Coverts bytes data to base64 data
    """
    try:
        return b64encode(data).decode()
    except Exception as e:
        print("ERROR: ", e)


@app.template_filter("formId")
def formId(dt: str) -> str:
    return dt.replace(" ", "-")


def welcome_projects():
    projects = Project.query.all()[:4]
    return [asserts.project_parser(pj) for pj in projects]


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
