"""
HrVr Digital Solutions - Flask Web Application
Author: HrVr Digital Solutions
Description: Professional Coding & Development Service Website
"""
from flask_mail import Mail, Message
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = "hrvr_digital_solutions_2026"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jyotiraikwar009@gmail.com'
app.config['MAIL_PASSWORD'] = 'gslh phyg vatv tfax'
app.config['MAIL_DEFAULT_SENDER'] = 'jyotiraikwar009@gmail.com'

mail = Mail(app)
@app.route("/send-mail")
def send_mail():
    msg = Message(
        subject="Test Mail",
        recipients=["sourabhkr512@gmail.com"],
        body="Hello Jyoti 🚀 Mail working!"
    )
    mail.send(msg)
    return "Mail Sent Successfully!"
# ─────────────────────────────────────────────
# Portfolio / Services Data
# ─────────────────────────────────────────────

TECH_STACK = {
    "Web Development": {
        "icon": "🌐",
        "skills": ["HTML5", "CSS3", "JavaScript", "PHP", "MySQL",
                   "Management Systems (Hospital, Library, School)"]
    },
    "UI/UX & Design": {
        "icon": "🎨",
        "skills": ["Figma UI/UX Design", "Web Design (Modern & Responsive)",
                   "App UI Design"]
    },
    "Backend & Database": {
        "icon": "🛢️",
        "skills": ["Core PHP & MySQL", "Database-Driven Web Apps",
                   "API Integration"]
    },
    "Mobile & Automation": {
        "icon": "📱",
        "skills": ["Android & iOS Mobile Apps", "Python Automations & Scripts",
                   "Custom Python Tools"]
    }
}

SERVICES = [
    {"title": "Custom Business Websites",     "icon": "💼", "desc": "Professional websites tailored to your brand & business needs."},
    {"title": "Personal Portfolio Websites",  "icon": "👤", "desc": "Showcase your work with a stunning, modern portfolio site."},
    {"title": "Management Systems",           "icon": "🏥", "desc": "School, Library, Hospital — complete management solutions."},
    {"title": "Database-driven Web Apps",     "icon": "🗄️", "desc": "Full-stack applications powered by robust database backends."},
    {"title": "Python Automations & Scripts", "icon": "🐍", "desc": "Automate repetitive tasks and build powerful Python tools."},
    {"title": "Android & iOS Mobile Apps",    "icon": "📱", "desc": "Cross-platform mobile apps for your business idea."},
    {"title": "UI/UX Design in Figma",        "icon": "🎨", "desc": "Beautiful, user-friendly designs crafted in Figma."},
    {"title": "API Integration",              "icon": "🔗", "desc": "Seamless third-party API connections for your applications."},
]

PROJECTS = [
    {"name": "Hospital Management System",  "tech": "PHP, MySQL, HTML5", "icon": "🏥", "status": "Completed"},
    {"name": "Library Management Portal",   "tech": "Python, Flask, SQLite","icon": "📚", "status": "Completed"},
    {"name": "E-Commerce Website",          "tech": "HTML5, JS, PHP",     "icon": "🛒", "status": "Completed"},
    {"name": "Portfolio Builder App",       "tech": "Python, Flask",       "icon": "💼", "status": "Completed"},
    {"name": "School ERP System",           "tech": "PHP, MySQL, JS",      "icon": "🏫", "status": "In Progress"},
    {"name": "Automation Bot Suite",        "tech": "Python, Selenium",    "icon": "🤖", "status": "Completed"},
]

MESSAGES = []   # In-memory store (replace with DB in production)

# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.route("/")
def home():
    return render_template("index.html",
                           tech_stack=TECH_STACK,
                           services=SERVICES,
                           projects=PROJECTS,
                           year=datetime.now().year)


@app.route("/services")
def services():
    return render_template("services.html",
                           services=SERVICES,
                           year=datetime.now().year)


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html",
                           projects=PROJECTS,
                           year=datetime.now().year)


@app.route("/contact")
def contact():
    return render_template("contact.html",
                           year=datetime.now().year)


@app.route("/api/contact", methods=["POST"])
def api_contact():
    """Handle contact form submissions."""
    data = request.get_json()
    name    = data.get("name", "").strip()
    email   = data.get("email", "").strip()
    project = data.get("project", "").strip()
    message = data.get("message", "").strip()

    if not all([name, email, message]):
        return jsonify({"success": False, "error": "Please fill all required fields."}), 400

    entry = {
        "id":        len(MESSAGES) + 1,
        "name":      name,
        "email":     email,
        "project":   project,
        "message":   message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    MESSAGES.append(entry)
    print(f"[NEW INQUIRY] From: {name} <{email}> | Project: {project}")
    return jsonify({"success": True,
                    "message": "Thank you! I will contact you soon. 🚀"})


@app.route("/api/stats")
def api_stats():
    """Return live stats for the website."""
    return jsonify({
        "projects_completed": 50,
        "happy_clients":      30,
        "tech_skills":        15,
        "years_experience":    3
    })


# ─────────────────────────────────────────────
# Run
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  🚀  HrVr Digital Solutions — Server Starting  🚀")
    print("=" * 55)
    print("  Open: http://127.0.0.1:5001")
    print("=" * 55)
    app.run(debug=True, host="0.0.0.0", port=5001)

    