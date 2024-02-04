from flask import Flask, render_template, render_template_string, url_for

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

qns = {
    "What is Python?": "Python is a versatile, high-level programming language known for its readability and simplicity. It acts like a reliable assistant, helping automate tasks and solve complex problems.",
    "What is HTML?": "HTML, or Hypertext Markup Language, serves as the foundation of web content. It's like a detailed blueprint, specifying how text, images, and links should be structured and organized on a webpage.",
    "What is CSS?": "CSS, or Cascading Style Sheets, is the stylist of the web. It adds flair to HTML by providing color, layout, and design, enhancing the visual appeal of websites.",
    "What is JavaScript?": "JavaScript is the interactive wizard of the web. It brings websites to life by enabling dynamic elements, like responsive buttons and live updates, making the online experience engaging.",
    "What is SQL?": "SQL, or Structured Query Language, is the librarian of databases. It's a language for managing and organizing information in digital libraries, making data retrieval and storage efficient.",
    "What is Golang?": "Golang, or Go, is a programming language designed for efficiency. It acts like a fast courier, delivering tasks in a clean and organized manner, making it suitable for building scalable and reliable software.",
    "What is C?": "C is the foundation of computer languages. It serves as the architect, constructing the intricate structure of software. C allows computers to understand and execute tasks effectively, making it a powerful language.",
    "What is GitHub?": "GitHub is like a collaborative workspace for programmers. It's a platform where individuals and teams store, manage, and share their code. Think of it as a digital hub that fosters collaboration and version control in software development.",
    "What is a Coding Platform?": "A coding platform is an online space where programmers write, test, and execute their code. It provides an environment for coding challenges, projects, and collaborative coding. Think of it as a virtual playground for developers to practice and showcase their skills.",
}


@app.route("/")
def home():
    return render_template("home.html", skills=skills, projects=projects)


@app.route("/projects")
def projects_():
    return render_template("projects.html")


@app.route("/faqs")
def faqs():
    return render_template("faqs.html", qns=qns)


@app.route("/a")
def a():
    return render_template_string(
        """
  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
        h1 {
            font-size: 90px;
            white-space: nowrap;
            overflow: hidden;
            animation: typewriter 2s steps(13) forwards,
                        blink 800ms steps(13) 2 normal forwards;
            border-right: 5px solid blue;
        }

        @keyframes typewriter {
            from {
                width: 0%;
            }
            to {
                width: 100%;
            }
        }

        @keyframes blink {
            0%, 100% {
                border-color: black;
            }
            50% {
                border-color: transparent;
            }
        }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>

                                  """
    )


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


if __name__ == "__main__":
    app.run(debug=True)
