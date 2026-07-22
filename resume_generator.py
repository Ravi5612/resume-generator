"""
==============================================
  RAVI RAI - Professional Resume Generator
  Design: Matches original resume style
  Run: python resume_generator.py
==============================================
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    Paragraph, Spacer, Table, TableStyle,
    HRFlowable, Frame, PageTemplate, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import BaseDocTemplate
import os


# ================================================================
#   RESUME DATA - RAVI RAI
# ================================================================

RESUME_DATA = {
    "personal": {
        "name": "RAVI RAI",
        "title": "Full Stack Developer",
        "email": "ravirai84272@gmail.com",
        "phone": "+91 6239408981",
        "location": "Sec 75, Mohali",
        "github": "github.com/Ravi5612",
    },
    "objective": (
        "To work as a Full Stack Developer where I can utilize my technical expertise in frontend and "
        "backend technologies, real-time web applications, and cloud deployment to contribute effectively "
        "to an organization. Committed to continuous learning and applying modern technologies to develop "
        "scalable, high-performance, and secure applications."
    ),
    "summary": [
        "Full Stack Developer with 1.5 years of professional experience and 6 months of internship experience.",
        "Expertise in React.js, Next.js, Node.js, Express.js, TypeScript, MongoDB, and PostgreSQL.",
        "Hands-on experience with real-time communication using Socket.io, and payment integration with Stripe.",
        "Proficient in cloud deployment and CI/CD pipelines with AWS, Vercel, and Hostinger.",
        "Developed and deployed scalable web applications including streaming and dating platforms.",
        "NCC Cadet bringing discipline, teamwork, and leadership skills to professional environments.",
    ],
    "skills": {
        "Frontend":      "HTML, CSS, JavaScript (ES6+), React.js, Next.js, Tailwind CSS, Bootstrap",
        "Backend":       "Node.js, Express.js, TypeScript, REST APIs, Socket.io, Authentication",
        "Database":      "MongoDB (NoSQL), PostgreSQL (SQL), Database Design, Query Optimization",
        "Tools & Cloud": "AWS (EC2, S3), Vercel, Hostinger, GoDaddy, Git, Github, CI/CD, Stripe API, Razorpay",
        "Other":         "Python, Django, WordPress, Problem-solving, Performance Optimization, Agile Methodology",
    },
    "experience": [
        {
            "role": "Full Stack Developer Intern",
            "company": "Hoping Mind",
            "duration": "November 2024 – February 2025",
            "description": (
                "Developed E-commerce website using React.js, Node.js, and Bootstrap. "
                "Created reusable components and integrated backend APIs."
            ),
            "points": [
                "Created responsive e-commerce platform with React.js and Bootstrap.",
                "Developed reusable components and integrated RESTful APIs.",
                "Deployed on Hostinger for production testing.",
                "Used Git/GitHub for version control and team collaboration.",
            ],
        },
        {
            "role": "Full Stack Developer",
            "company": "Kodvidya Technology Pvt. Ltd.",
            "duration": "March 2025 – December 2025",
            "description": (
                "Developed Busker Live Streaming Platform using Next.js, Node.js, and TypeScript. "
                "Implemented real-time coin transaction system and integrated Stripe API for secure payments."
            ),
            "points": [
                "Built real-time coin transaction system using Socket.io for instant user-to-artist rewards.",
                "Integrated Stripe API for secure payments and wallet management.",
                "Deployed on AWS and Vercel with CI/CD pipelines.",
                "Optimized performance for high traffic and low latency applications.",
            ],
        },
        {
            "role": "Full Stack Developer",
            "company": "RG Startup – Web Solution",
            "duration": "December 2025 – Present",
            "description": (
                "Working on Astrology in Bharat – a role-based astrology services platform similar to AstroTalk, "
                "built with Next.js and NestJS following Domain Driven Architecture (DDA). Features multi-role "
                "architecture with Normal Users, Experts, Merchants, Sub Admins, and Super Admin."
            ),
            "points": [
                "Developed role-based access system with Normal User, Expert, Merchant, Sub Admin, and Super Admin roles.",
                "Normal Users can browse and book astrology sessions with verified experts on the platform.",
                "Experts manage their profiles, set availability, and provide astrology consultation services.",
                "Merchants can list and sell astrology-related products through the integrated marketplace.",
                "Super Admin has full control over platform management, user moderation, and Sub Admin creation.",
                "Built scalable backend architecture to handle multi-role permissions and workflows.",
            ],
        },
    ],
    "projects": [
        {
            "name": "Busker - Live Streaming Platform",
            "url": "thebusker.pro",
            "description": (
                "Comprehensive live streaming platform enabling artists to perform and earn through "
                "real-time coin transactions."
            ),
            "points": [
                "Real-time coin accumulation system using Socket.io.",
                "Stripe integration for payments and wallet top-ups.",
                "Built with Next.js, Tailwind CSS, Node.js, TypeScript.",
                "Deployed on AWS and Vercel with CI/CD pipelines.",
            ],
        },
        {
            "name": "GoVelvet - Dating Application",
            "url": "govelvet.co",
            "description": (
                "Full-featured dating application with user authentication, profile management, "
                "and real-time chat functionality."
            ),
            "points": [
                "Real-time chat functionality using WebSockets.",
                "User authentication and profile management system.",
                "Responsive UI with React.js and Tailwind CSS.",
                "RESTful APIs with Node.js and Express.js.",
                "MongoDB for flexible data storage.",
            ],
        },
    ],
    "education": [
        {
            "degree": "B.Tech in Computer Science & Engineering",
            "institution": "Gulzar Group of Institutes, Punjab",
            "year": "2021 – 2025",
            "grade": "",
        },
        {
            "degree": "12th (Senior Secondary)",
            "institution": "S.D.P. Senior Secondary School",
            "year": "2020",
            "grade": "78%",
        },
        {
            "degree": "10th (Matriculation)",
            "institution": "Red Rose Model Senior Secondary School",
            "year": "2018",
            "grade": "86%",
        },
    ],
    "achievements": [
        "NCC Cadet: 3 Punjab Battalion & 19 Punjab Battalion – Leadership and discipline training.",
        "Completed 6-month MEAN Stack Development Internship at Hoping Mind.",
        "Successfully developed and deployed Busker Live Streaming Platform with real-time features.",
        "Developed and deployed GoVelvet Dating Application with real-time chat functionality.",
        "Implemented CI/CD pipelines for continuous integration and deployment.",
        "Experience in optimizing web applications for high traffic and performance.",
    ],
    "personal_details": {
        "Date of Birth": "6 September 2003",
        "Gender":        "Male",
        "Languages":     "English, Hindi, Punjabi",
        "Nationality":   "Indian",
        "Interests":     "Technology, Programming, Web Development, Problem Solving",
    },
}


# ================================================================
#   COLORS
# ================================================================

HEADER_BG      = colors.HexColor("#1a7a8f")
HEADER_TEXT    = colors.white
SECTION_COLOR  = colors.HexColor("#1a7a8f")
COMPANY_COLOR  = colors.HexColor("#1a6faa")
TEXT_DARK      = colors.HexColor("#1a1a1a")
TEXT_BODY      = colors.HexColor("#333333")
TEXT_LIGHT     = colors.HexColor("#555555")
DIVIDER        = colors.HexColor("#1a7a8f")
ROW_BG         = colors.HexColor("#f0f8fa")


# ================================================================
#   STYLES
# ================================================================

def build_styles():
    return {
        "header_name": ParagraphStyle(
            "header_name", fontName="Helvetica-Bold", fontSize=27,
            textColor=HEADER_TEXT, leading=33, alignment=TA_CENTER,
        ),
        "header_title": ParagraphStyle(
            "header_title", fontName="Helvetica", fontSize=13,
            textColor=colors.HexColor("#d0f0f8"), leading=18, alignment=TA_CENTER,
        ),
        "header_contact": ParagraphStyle(
            "header_contact", fontName="Helvetica", fontSize=9,
            textColor=colors.HexColor("#e8f8fc"), leading=14, alignment=TA_CENTER,
        ),
        "section": ParagraphStyle(
            "section", fontName="Helvetica-Bold", fontSize=11,
            textColor=SECTION_COLOR, leading=15, spaceBefore=8, spaceAfter=2,
            letterSpacing=0.8,
        ),
        "company": ParagraphStyle(
            "company", fontName="Helvetica-Bold", fontSize=10.5,
            textColor=COMPANY_COLOR, leading=15,
        ),
        "role": ParagraphStyle(
            "role", fontName="Helvetica-Bold", fontSize=9.5,
            textColor=TEXT_DARK, leading=14,
        ),
        "duration": ParagraphStyle(
            "duration", fontName="Helvetica", fontSize=9,
            textColor=TEXT_LIGHT, leading=13, alignment=TA_RIGHT,
        ),
        "exp_desc": ParagraphStyle(
            "exp_desc", fontName="Helvetica", fontSize=9.5,
            textColor=TEXT_BODY, leading=14, spaceAfter=2,
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName="Helvetica", fontSize=9.5,
            textColor=TEXT_BODY, leading=14, leftIndent=10, spaceAfter=1,
        ),
        "body": ParagraphStyle(
            "body", fontName="Helvetica", fontSize=9.5,
            textColor=TEXT_BODY, leading=15, alignment=TA_JUSTIFY,
        ),
        "skill_label": ParagraphStyle(
            "skill_label", fontName="Helvetica-Bold", fontSize=9.5,
            textColor=TEXT_DARK, leading=14,
        ),
        "skill_value": ParagraphStyle(
            "skill_value", fontName="Helvetica", fontSize=9.5,
            textColor=TEXT_BODY, leading=14,
        ),
        "edu_degree": ParagraphStyle(
            "edu_degree", fontName="Helvetica-Bold", fontSize=10,
            textColor=COMPANY_COLOR, leading=14,
        ),
        "edu_inst": ParagraphStyle(
            "edu_inst", fontName="Helvetica", fontSize=9.5,
            textColor=TEXT_BODY, leading=14,
        ),
        "project_url": ParagraphStyle(
            "project_url", fontName="Helvetica-Oblique", fontSize=9,
            textColor=TEXT_LIGHT, leading=13,
        ),
        "personal_label": ParagraphStyle(
            "personal_label", fontName="Helvetica-Bold", fontSize=9.5,
            textColor=TEXT_DARK, leading=15,
        ),
        "personal_value": ParagraphStyle(
            "personal_value", fontName="Helvetica", fontSize=9.5,
            textColor=TEXT_BODY, leading=15,
        ),
    }


# ================================================================
#   HELPERS
# ================================================================

def section_title(text, styles):
    return [
        Spacer(1, 2),
        Paragraph(text, styles["section"]),
        HRFlowable(width="100%", thickness=1.0, color=DIVIDER,
                   spaceBefore=1, spaceAfter=3),
    ]


def two_col(left, right, left_pct="72%", right_pct="28%"):
    t = Table([[left, right]], colWidths=[left_pct, right_pct])
    t.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("TOPPADDING",    (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


# ================================================================
#   SECTIONS
# ================================================================

def build_header(data, styles):
    p = data["personal"]
    contact_line = (
        f"{p['email']}  |  {p['phone']}  |  "
        f"{p['location']}  |  {p['github']}"
    )
    header_content = [
        [Paragraph(p["name"], styles["header_name"])],
        [Paragraph(p["title"], styles["header_title"])],
        [Spacer(1, 4)],
        [Paragraph(contact_line, styles["header_contact"])],
    ]
    inner = Table(header_content, colWidths=["100%"])
    inner.setStyle(TableStyle([
        ("LEFTPADDING",   (0, 0), (-1, -1), 0),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 0),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
    ]))
    outer = Table([[inner]], colWidths=["100%"])
    outer.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), HEADER_BG),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("TOPPADDING",    (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return [outer, Spacer(1, 4)]


def build_objective(data, styles):
    return section_title("CAREER OBJECTIVE", styles) + [
        Paragraph(data["objective"], styles["body"]),
    ]


def build_summary(data, styles):
    items = section_title("PROFESSIONAL SUMMARY", styles)
    for point in data["summary"]:
        items.append(Paragraph(f"–  {point}", styles["bullet"]))
    return items


def build_skills(data, styles):
    items = section_title("TECHNICAL SKILLS", styles)
    rows = []
    for label, value in data["skills"].items():
        rows.append([
            Paragraph(f"{label}:", styles["skill_label"]),
            Paragraph(value, styles["skill_value"]),
        ])
    t = Table(rows, colWidths=["17%", "83%"])
    t.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 2),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("TOPPADDING",    (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    items.append(t)
    return items


def build_experience(data, styles):
    items = section_title("WORK EXPERIENCE", styles)
    for exp in data["experience"]:
        items.append(two_col(
            Paragraph(exp["role"], styles["company"]),
            Paragraph(exp["duration"], styles["duration"]),
        ))
        items.append(Paragraph(exp["company"], styles["role"]))
        items.append(Spacer(1, 2))
        items.append(Paragraph(exp["description"], styles["exp_desc"]))
        for pt in exp["points"]:
            items.append(Paragraph(f"–  {pt}", styles["bullet"]))
        items.append(Spacer(1, 4))
    return items


def build_projects(data, styles):
    items = section_title("KEY PROJECTS", styles)
    for proj in data["projects"]:
        block = []
        block.append(Paragraph(proj["name"], styles["company"]))
        block.append(Paragraph(proj["url"], styles["project_url"]))
        block.append(Spacer(1, 1))
        block.append(Paragraph(proj["description"], styles["exp_desc"]))
        for pt in proj["points"]:
            block.append(Paragraph(f"–  {pt}", styles["bullet"]))
        block.append(Spacer(1, 4))
        items.append(KeepTogether(block))
    return items


def build_education(data, styles):
    items = section_title("EDUCATION", styles)
    for edu in data["education"]:
        block = []
        block.append(two_col(
            Paragraph(edu["degree"], styles["edu_degree"]),
            Paragraph(edu["year"], styles["duration"]),
        ))
        block.append(Paragraph(
            f"{edu['institution']}  {('|  ' + edu['grade']) if edu['grade'] else ''}",
            styles["edu_inst"],
        ))
        block.append(Spacer(1, 3))
        items.append(KeepTogether(block))
    return items


def build_achievements(data, styles):
    items = section_title("ACHIEVEMENTS & CERTIFICATIONS", styles)
    for ach in data["achievements"]:
        items.append(Paragraph(f"–  {ach}", styles["bullet"]))
    return items


def build_personal(data, styles):
    items = section_title("PERSONAL DETAILS", styles)
    rows = []
    for label, value in data["personal_details"].items():
        rows.append([
            Paragraph(f"{label}:", styles["personal_label"]),
            Paragraph(value, styles["personal_value"]),
        ])
    t = Table(rows, colWidths=["20%", "80%"])
    t.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 2),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 4),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    items.append(t)
    return items


# ================================================================
#   PAGE TEMPLATE
# ================================================================

class ResumeDoc(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        pw, ph = A4
        lm = kwargs.get("leftMargin", 15 * mm)
        rm = kwargs.get("rightMargin", 15 * mm)
        tm = kwargs.get("topMargin", 12 * mm)
        bm = kwargs.get("bottomMargin", 15 * mm)
        frame = Frame(
            lm, bm, pw - lm - rm, ph - tm - bm,
            id="body",
            leftPadding=0, rightPadding=0,
            topPadding=0, bottomPadding=0,
        )
        self.addPageTemplates([
            PageTemplate(id="main", frames=[frame], onPage=self._page_footer)
        ])

    @staticmethod
    def _page_footer(canvas_obj, doc):
        pw, ph = A4
        canvas_obj.setFont("Helvetica", 7)
        canvas_obj.setFillColor(colors.HexColor("#999999"))
        canvas_obj.drawCentredString(pw / 2, 8 * mm, f"Page {doc.page}")


# ================================================================
#   GENERATE PDF
# ================================================================

def generate_resume(output_path="Ravi_Rai_Resume.pdf"):
    doc = ResumeDoc(
        output_path,
        pagesize=A4,
        leftMargin=12 * mm,
        rightMargin=12 * mm,
        topMargin=8 * mm,
        bottomMargin=10 * mm,
        title="Resume – Ravi Rai",
        author="Ravi Rai",
        subject="Full Stack Developer Resume",
    )

    styles = build_styles()
    story = (
        build_header(RESUME_DATA, styles)
        + build_objective(RESUME_DATA, styles)
        + build_summary(RESUME_DATA, styles)
        + build_skills(RESUME_DATA, styles)
        + build_experience(RESUME_DATA, styles)
        + build_projects(RESUME_DATA, styles)
        + build_education(RESUME_DATA, styles)
        + build_achievements(RESUME_DATA, styles)
        + build_personal(RESUME_DATA, styles)
    )

    doc.build(story)
    abs_path = os.path.abspath(output_path)
    print(f"\n  Resume PDF generated successfully!")
    print(f"  Saved at: {abs_path}\n")
    return abs_path


# ================================================================
#   ENTRY POINT
# ================================================================

if __name__ == "__main__":
    print("Generating Ravi Rai's Resume...")
    generate_resume("Ravi_Rai_Resume.pdf")
