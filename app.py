from flask import Flask, render_template, request
from datetime import date
from resume import ed_experiences, w_experiences
from project_details import *
from joblib import load
from sklearn.preprocessing import LabelEncoder
import numpy as np

app = Flask(__name__)

title = "Simone Martin"

now = date.today()
current_year = now.year
email = "martin.s.marotta@gmail.com"
location = "Naples, IT"
skype = "martin.s.marotta@gmail.com"

social_buttons = [
    # url, href class, i class
    ("https://github.com/c0pper/", "github", "bx bxl-github"),
    ("https://www.instagram.com/sim01110011.01101001.01101101/", "instagram", "bx bxl-instagram"),
    ("https://www.youtube.com/channel/UCtUNRX-B_j2ipkL1Lihih8w/", "youtube", "bx bxl-youtube"),
    ("https://www.facebook.com/Simooon/", "facebook", "bx bxl-facebook")
]

navmenu = [
    ("#hero", "bx bx-home", "Home"),
    ("#about", "bx bx-user", "About"),
    ("#skills", "bx bx-user", "Skills"),
    ("#resume", "bx bx-file-blank", "Resume"),
    ("#projects", "bx bx-book-content", "Projects"),
    ("#contact", "bx bx-envelope", "Contact")
]

lang_skills = [("english", 100), ("Russian", 70), ("SPANISH", 30), ("FRENCH", 30), ("JAPANESE", 20)]
comp_skills = [("PHOTOSHOP", 80), ("HTML", 70), ("PYTHON", 50), ("WORDPRESS/CMS", 50), ("CSS", 30)]

projects = [  # Title, img, url, cat
    (mirco["title"], "mirco.png", mirco["internal_url"], mirco["cat"]),
    (zettibot["title"], "zettibot.png", zettibot["internal_url"], zettibot["cat"]),
    (pers_website["title"], "personal_website.png", pers_website["internal_url"], pers_website["cat"]),
    (python_cv["title"], "pycv.png", python_cv["internal_url"], python_cv["cat"]),
    (anime_scraper["title"], "animedownloader.png", anime_scraper["internal_url"], anime_scraper["cat"]),
    # ("Text Collection", "karman.png", "text-collection"),
    (karman_line["title"], "karman.png", karman_line["internal_url"], karman_line["cat"]),
    (win95_site["title"], "win95.png", win95_site["internal_url"], win95_site["cat"]),
    (spacex_it["title"], "starman.png", spacex_it["internal_url"], spacex_it["cat"]),
    (gta_napoli["title"], "gta.png", gta_napoli["internal_url"], gta_napoli["cat"]),
    (unidia["title"], "unidia.png", unidia["internal_url"], unidia["cat"]),
    (mirai_subs["title"], "mirai.png", mirai_subs["internal_url"], mirai_subs["cat"]),
    (clients_app["title"], "clients.png", clients_app["internal_url"], clients_app["cat"]),
    (nmusic_app["title"], "nmusic.png", nmusic_app["internal_url"], nmusic_app["cat"])
]


def build_projects_navmenu():
    projects_navmenu = [("/", "bx bx-home", "Home")]
    for p in projects:
        nav_url = p[2]
        nav_icon = "bi bi-box-seam"
        nav_title = p[0]
        nav_element = (nav_url, nav_icon, nav_title)
        projects_navmenu.append(nav_element)

    return(projects_navmenu)


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    return age


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        s = request.form["testo"]

        lbl_enc = LabelEncoder()
        lbl_enc.classes_ = np.load('classes.npy', allow_pickle=True)
        tfv = load('tfv.joblib')
        clf2 = load('logreg.joblib')

        s_tfv = tfv.transform([s])

        prediction = lbl_enc.inverse_transform(clf2.predict(s_tfv))
    else:
        prediction = ""

    return render_template(
        "index.html",
        title=title,
        social_buttons=social_buttons,
        navmenu=navmenu,
        email=email,
        location=location,
        skype=skype,
        age=calculateAge(date(1993, 9, 4)),
        copyright_year=current_year,
        lang_skills=lang_skills,
        comp_skills=comp_skills,
        ed_experiences=ed_experiences,
        w_experiences=w_experiences,
        projects=projects,
        prediction=prediction
    )


@app.route(mirco["internal_url"])
def mirco_website():
    return render_template(
        "project_base.html",
        title=mirco["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=mirco
    )


@app.route(zettibot["internal_url"])
def zettibot_ai():
    return render_template(
        "project_base.html",
        title=zettibot["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=zettibot
    )


@app.route(pers_website["internal_url"])
def personal_website():
    return render_template(
        "project_base.html",
        title=pers_website["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=pers_website
    )


@app.route(python_cv["internal_url"])
def pyCV():
    return render_template(
        "project_base.html",
        title=python_cv["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=python_cv
    )


@app.route(anime_scraper["internal_url"])
def anime_downloader():
    return render_template(
        "project_base.html",
        title=anime_scraper["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=anime_scraper
    )


@app.route(text_collect["internal_url"])
def text_collection():
    return render_template(
        "project_base.html",
        title=text_collect["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=text_collect
    )


@app.route(karman_line["internal_url"])
def karman():
    return render_template(
        "project_base.html",
        title=karman_line["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=karman_line
    )


@app.route(win95_site["internal_url"])
def win95():
    return render_template(
        "project_base.html",
        title=win95_site["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=win95_site
    )


@app.route(spacex_it["internal_url"])
def spacex():
    return render_template(
        "project_base.html",
        title=spacex_it["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=spacex_it
    )


@app.route(gta_napoli["internal_url"])
def gta():
    return render_template(
        "project_base.html",
        title=gta_napoli["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=gta_napoli
    )


@app.route(unidia["internal_url"])
def uni():
    return render_template(
        "project_base.html",
        title=unidia["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=unidia
    )


@app.route(mirai_subs["internal_url"])
def mirai():
    return render_template(
        "project_base.html",
        title=mirai_subs["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=mirai_subs
    )


@app.route(clients_app["internal_url"])
def clients():
    return render_template(
        "project_base.html",
        title=clients_app["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=clients_app
    )


@app.route(nmusic_app["internal_url"])
def nmusic():
    return render_template(
        "project_base.html",
        title=nmusic_app["title"],
        copyright_year=current_year,
        social_buttons=social_buttons,
        navmenu=build_projects_navmenu(),
        data=nmusic_app
    )


if __name__ == "__main__":
    app.run(debug=True)
