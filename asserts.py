# project = {
#     "title": "project1",
#     "img_path": "imgs/photo-1572177812156-58036aae439c",
#     "desc": "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
#     "details": "TEST Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.",
#     "project_url": "#",
#     "github_url": "#",
# }

from models import Certificate, Coding_Platform, FAQs, Project, Skill, db


class Asserts:
    def __init__(self) -> None:
        ...

    @property
    def skills(self) -> dict:
        # skills = {
        #     "python": 90,
        #     "Go Lang": 60,
        #     "C": 40,
        #     "CSS": 50,
        #     "HTML": 92,
        #     "JavaScript": 74,
        #     "SQL": 80,
        # }
        data = Skill.query.all()
        skills_ = {skl.skill: skl.percentage for skl in data}

        return skills_

    def project_parser(self, pj: Project) -> dict[str, str | bytes]:
        return {
            "title": pj.title,
            "image": pj.image,
            "desc": pj.desc,
            "details": pj.details,
            "project_url": pj.project_url,
            "github_url": pj.github_url,
        }

    @property
    def projects(self) -> list[dict[str, str | bytes]]:
        projects_ = Project.query.all()
        return [self.project_parser(pj) for pj in projects_]

    def cert_parser(self, cert: Certificate) -> dict[str, str | bytes]:
        return {
            "title": cert.title,
            "image": cert.image,
            "iss_org": cert.iss_org,
            "date": cert.date,
        }

    @property
    def certificates(self):
        certificates_ = Certificate.query.all()
        return [self.cert_parser(cert) for cert in certificates_]

    @property
    def faqs(self) -> dict[str, str]:
        # qns = {
        #     "What is Python?": "Python is a versatile, high-level programming language known for its readability and simplicity. It acts like a reliable assistant, helping automate tasks and solve complex problems.",
        #     "What is HTML?": "HTML, or Hypertext Markup Language, serves as the foundation of web content. It's like a detailed blueprint, specifying how text, images, and links should be structured and organized on a webpage.",
        #     "What is CSS?": "CSS, or Cascading Style Sheets, is the stylist of the web. It adds flair to HTML by providing color, layout, and design, enhancing the visual appeal of websites.",
        #     "What is JavaScript?": "JavaScript is the interactive wizard of the web. It brings websites to life by enabling dynamic elements, like responsive buttons and live updates, making the online experience engaging.",
        #     "What is SQL?": "SQL, or Structured Query Language, is the librarian of databases. It's a language for managing and organizing information in digital libraries, making data retrieval and storage efficient.",
        #     "What is Golang?": "Golang, or Go, is a programming language designed for efficiency. It acts like a fast courier, delivering tasks in a clean and organized manner, making it suitable for building scalable and reliable software.",
        #     "What is C?": "C is the foundation of computer languages. It serves as the architect, constructing the intricate structure of software. C allows computers to understand and execute tasks effectively, making it a powerful language.",
        #     "What is GitHub?": "GitHub is like a collaborative workspace for programmers. It's a platform where individuals and teams store, manage, and share their code. Think of it as a digital hub that fosters collaboration and version control in software development.",
        #     "What is a Coding Platform?": "A coding platform is an online space where programmers write, test, and execute their code. It provides an environment for coding challenges, projects, and collaborative coding. Think of it as a virtual playground for developers to practice and showcase their skills.",
        # }

        data = FAQs.query.all()
        faqns = {fqn.question: fqn.answer for fqn in data}
        return faqns

    @property
    def coding_platforms(self) -> list[dict[str, str]]:
        coding_platforms_ = Coding_Platform.query.all()
        return [{"name": cp.name, "link": cp.link} for cp in coding_platforms_]


def RI(path):
    with open(path, "rb") as f:
        return f.read()


projects_data = [
    (
        "Task Manager",
        RI("./FF/task_manager.jpg"),
        "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
        "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.",
        "#",
        "#",
    ),
    (
        "Notes Keeper",
        RI("./FF/Note_web.png"),
        "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
        "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.",
        "#",
        "#",
    ),
    (
        "Portfolio",
        RI("./FF/portfolio.jpg"),
        "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
        "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.",
        "#",
        "#",
    ),
    (
        "USD-UGX Rate Tracker",
        RI("./FF/USD-UGX.jpg"),
        "Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.",
        "Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.",
        "#",
        "#",
    ),
]

certificates_data = [
    (
        "Intro to Python",
        RI("Introduction to Python_certificate.jpg"),
        "SoloLearn",
        "2023-11-03",
    ),
    (
        "Intro to JS",
        RI("60fba675-0a5d-4b5c-9cd5-0546b3e1dc4b.png"),
        "SoloLearn",
        "2023-10-11",
    ),
    (
        "Intro to ML",
        RI("Kibuule Noah - Intro to Machine Learning.png"),
        "Kaggle",
        "2023-02-09",
    ),
    (
        "Intermediate ML",
        RI("Kibuule Noah - Intermediate Machine Learning.png"),
        "Kaggle",
        "2023-03-12",
    ),
    (
        "Intermediate JS",
        RI("JavaScript Intermediate_certificate.jpg"),
        "SoloLearn",
        "2023-10-11",
    ),
    ("Intermediate C", RI("C Intermediate_certificate.jpg"), "SoloLearn", "2023-10-12"),
    (
        "Intermediate Python",
        RI("Python Intermediate_certificate.jpg"),
        "SoloLearn",
        "2023-10-04",
    ),
    ("Python", RI("Kibuule Noah - Python.png"), "Kaggle", "2023-04-14"),
    (
        "FrontEnd-HTML",
        RI("Kibuule_Noah20230901-72-kc0ndb.jpg"),
        "GreatLearning",
        "2023-09-10",
    ),
    ("Pandas", RI("Kibuule Noah - Pandas.png"), "Kaggle", "2023-02-19"),
    (
        "Data Visualization",
        RI("Kibuule Noah - Data Visualization.png"),
        "Kaggle",
        "2023-04-12",
    ),
    (
        "Feature Engineering",
        RI(
            "Kibuule Noah - Feature Engineering.png",
        ),
        "Kaggle",
        "2023-04-24",
    ),
    ("Time Series", RI("Kibuule Noah - Time Series.png"), "Kaggle", "2023-07-06"),
]


def rebuild_projects_table() -> None:
    """
    But you must have to clear the table first and make
    it blank to get the expected resluts
    """
    for pj_d in projects_data:
        pj = Project(*pj_d)
        db.session.add(pj)
    db.session.commit()


def rebuild_certificate_table() -> None:
    """
    But you must have to clear the table first and make
    it blank to get the expected resluts
    """
    for dt in certificates_data:
        cert = Certificate(*dt)
        db.session.add(cert)
        db.session.commit()


print("Yooooooooo Yooooooooo Yooooooooo Yooooooooo")
