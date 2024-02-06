from models import Coding_Platform, FAQs, db, Certificate, Skill, Project


def add_skill(skill: str, per: int) -> None:
    new_skill = Skill(skill, per)
    db.session.add(new_skill)
    db.session.commit()


def add_cert(title: str, image: bytes, iss_org: str, date: str) -> None:
    new_cert = Certificate(title, image, iss_org, date)
    db.session.add(new_cert)
    db.session.commit()


def add_project(
    title: str, image: bytes, desc: str, details: str, project_url: str, github_url: str
) -> None:
    new_project = Project(title, image, desc, details, project_url, github_url)
    db.session.add(new_project)
    db.session.commit()


def add_faq(question: str, answer: str) -> None:
    new_qn = FAQs(question, answer)
    db.session.add(new_qn)
    db.session.commit()


def add_coding_platform(name: str, link: str) -> None:
    new_ptf = Coding_Platform(name, link)
    db.session.add(new_ptf)
    db.session.commit()


def update_(table: str = "jk",id_:int,new_value):
    """
    # Updates user name given then new name doesn't exists
    """
    db_table = None
    match table:
        case "skills":
            db_table = Skill
        case "certificates":
            db_table = Certificate
        case "projects":
            db_table = Project
        case "faqs":
            db_table = FAQs
        case "coding_platform":
            db_table = Coding_Platform
    if db_table:
        db_table.query.filter_by(id=id_).update({.name: new_name})
        db.session.commit()
        return
