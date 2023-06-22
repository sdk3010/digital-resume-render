from pathlib import Path

import streamlit as st

from PIL import Image

# ---- path settings---

css_file = "styles/main.css"
resume_file =  "assets/CV.pdf"
profile_pic = "assets/profile-pic.png"






# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | S Dhipesh Kumar"
PAGE_ICON = ":wave:"
NAME = "S Dhipesh Kumar"
DESCRIPTION = """
Data Analyst, 
"""
EMAIL = "dhipxxxx01@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/",
    "GitHub": "https://github.com/",
    "Hacker_Rank":"https://www.hackerrank.com/"
}
PROJECTS = ("""
-   Title : Salary Prediction Machine Learning,
-   Title : Exploratory Data Analysis on Real-Estate in Metropolitan cities""")






st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# st.title("hello there!")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# # --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
-  Sir Padampat Singhania University, Udaipur 2019-2023
B. Tech in Computer Science and Engineering (Cloud Technology and Information
Security)

-  Fresher extracting actionable insights from data.
-   Strong hands on experience and knowledge in Python.
-  Good understanding of statistical principles.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
-  Programming: Python (Numpy, Pandas, Matplotlib, Seaborn), SQL
-  Data Visulization: Tableau, MS Excel, Plotly
-  Databases: MySQL
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
PROJECTS
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")