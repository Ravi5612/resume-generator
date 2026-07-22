# Python Resume Generator 📄

A simple and elegant Python script to generate a professional PDF resume using the `reportlab` library. This script creates a well-structured, 2-page resume with a modern design (teal headers, neat spacing, and clear sections).

## Features
- Generates a PDF resume directly from a Python dictionary.
- Clean and professional layout (teal and white theme).
- Includes all standard resume sections: Objective, Summary, Skills, Work Experience, Projects, Education, Achievements, and Personal Details.
- Easy to update and customize.

## Prerequisites
- **Python 3.x** installed on your system.
- `reportlab` library for PDF generation.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ravi5612/resume-generator.git
   cd resume-generator
   ```

2. **Install the required library:**
   Run the following command to install `reportlab`:
   ```bash
   pip install reportlab
   ```

## How to Use

1. **Update your data:**
   Open `resume_generator.py` in your favorite code editor. At the top of the file, you will find a `RESUME_DATA` dictionary. Update the details (name, experience, skills, etc.) with your own information.

2. **Run the script:**
   Execute the script from your terminal:
   ```bash
   python resume_generator.py
   ```

3. **Check the output:**
   Once the script finishes running, it will generate a PDF file named `Ravi_Rai_Resume.pdf` (or whatever you specify as the output name) in the same directory.

## Customization
- **Colors:** You can change the theme colors by updating the hex codes in the `# COLORS` section of the script.
- **Fonts & Spacing:** Adjust the `build_styles()` function to tweak font sizes, leading (line spacing), and margins.

---
*Created by Ravi Rai*
