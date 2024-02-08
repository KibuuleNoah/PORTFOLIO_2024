from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    url_for,
)
from base64 import b64encode
from asserts import Asserts

from models import Message, Project, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///self/safe/database.db"
db.init_app(app)

asserts = Asserts()


@app.route("/")
def home():
    try:
        certificates = asserts.certificates
        display_certs = certificates[:4]
        hidden_certs = certificates[4:]
    except:
        display_certs, hidden_certs = [], []
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


@app.route("/vmsgs", methods=["GET", "POST"])
def view_messages():
    if request.method == "POST":
        password = request.form.get("adim-password", "")
        if password and password == "noport$$$":
            messages = Message.query.all()
            messages = [
                {
                    "name": obj.name,
                    "email": obj.email,
                    "message": obj.message,
                    "date": obj.datetime,
                }
                for obj in messages
            ]
            return render_template("messages.html", messages=messages)
    return "<h1>Adim<h1><form method='POST'><br><input type='password' name='adim-password' placeholder='adim password' required/></form>"


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


# if __name__ == "__main__":
# app.app_context().push()
# db.create_all()
# app.run(debug=True)
