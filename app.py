from flask import (
    Flask,
    jsonify,
    render_template,
    render_template_string,
    request,
    url_for,
)
from base64 import b64encode, b64decode
from asserts import Asserts
from models import Certificate, Message, Project, Skill, db, FAQs

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)

asserts = Asserts()


@app.route("/")
def home():
    # pj = Project.query.all()[0]
    # print(convert_to_base64(pj.image))
    # with open("./static/imgs/photo-1572177812156-58036aae439c", "rb") as f:
    #     f = f.read()
    #     project = Project(
    #         "test iiiiii",
    #         f,
    #         "testing...desc",
    #         "testing...details",
    #         "/just/testing",
    #         "/just/testing",
    #     )
    #     db.session.add(project)
    #     db.session.commit()
    # for k, v in asserts.skills.items():
    #     q = Skill(k, v)
    #     db.session.add(q)
    # db.session.commit()
    certificates = asserts.certificates
    certs_displayed = certificates[:4]
    certs_hidden = certificates[4:]
    return render_template(
        "home.html",
        skills=asserts.skills,
        certs_displayed=certs_displayed,
        certs_hidden=certs_hidden,
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
