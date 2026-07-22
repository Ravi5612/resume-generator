<div align="center">
  <h1>📄 Python Resume Generator</h1>
  <p><i>A sleek and professional PDF resume generator powered by Python & ReportLab.</i></p>
</div>

<br />

## 🌟 Features
- 🎨 **Elegant Design:** Beautiful teal headers, clean typography, and neat section dividers.
- 🖨️ **PDF Generation:** Outputs a ready-to-print, two-page PDF resume.
- 🛠️ **Easy Customization:** Update a single Python dictionary to generate a brand new resume.
- 🚀 **Fast & Lightweight:** Relies purely on the powerful `reportlab` library.

---

## 💻 Prerequisites
Make sure you have the following installed on your machine:
- 🐍 **Python 3.x**
- 📦 **Pip** (Python package installer)

---

## ⚙️ Installation

1️⃣ **Clone the repository:**
```bash
git clone https://github.com/Ravi5612/resume-generator.git
cd resume-generator
```

2️⃣ **Install the required dependencies:**
```bash
pip install reportlab
```

---

## 🚀 How to Use

📝 **1. Update Your Information:**
Open the `resume_generator.py` file in your favorite code editor (like VS Code). At the top, you'll find the `RESUME_DATA` dictionary. Swap out the placeholder text with your actual details:
- Personal Info (Name, Email, Phone, GitHub, etc.)
- Work Experience
- Education
- Skills & Projects

▶️ **2. Run the Script:**
Once your data is updated, open your terminal and run:
```bash
python resume_generator.py
```

🎉 **3. Get Your Resume:**
Boom! 💥 You will find your freshly generated PDF (e.g., `Ravi_Rai_Resume.pdf`) saved in the exact same directory. Open it up and admire your work!

---

## 🎨 Customizing the Look

Want to change the vibe? It's easy!
- 🌈 **Colors:** Scroll to the `# COLORS` section in the script. Update the hex codes (e.g., `#1a7a8f`) to match your personal brand.
- 📏 **Fonts & Spacing:** Check out the `build_styles()` function to tweak font sizes, leading (line spacing), and alignments.

---
<div align="center">
  <b>Built with ❤️ by Ravi Rai</b>
</div>
