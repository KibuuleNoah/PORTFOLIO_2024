from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    message = db.Column(db.String)

    def __init__(self, name: str, email: str, message: str) -> None:
        self.name = name
        self.email = email
        self.message = message


class Skill(db.Model):
    __tablename__ = "skils"
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String, unique=True)
    percentage = db.Column(db.Integer)

    def __init__(self, skill: str, percentage: int) -> None:
        self.skill = skill
        self.percentage = percentage


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    image = db.Column(db.LargeBinary, nullable=True)
    desc = db.Column(db.String)
    details = db.Column(db.String)
    project_url = db.Column(db.String)
    github_url = db.Column(db.String)

    def __init__(
        self,
        title: str,
        image: bytes,
        desc: str,
        details: str,
        project_url: str,
        github_url: str,
    ):
        self.title = title
        self.image = image
        self.desc = desc
        self.details = details
        self.project_url = project_url
        self.github_url = github_url


class Certificate(db.Model):
    __tablename__ = "certificates"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    iss_org = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    def __init__(self, title: str, image: bytes, iss_org: str, date: str):
        self.title = title
        self.image = image
        self.iss_org = iss_org
        self.date = date


class FAQs(db.Model):
    __tablename__ = "faqs"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)

    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer


class Coding_Platform(db.Model):
    __tablename__ = "coding_platform"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)

    def __init__(self, name: str, link: str) -> None:
        self.name = name
        self.link = link
