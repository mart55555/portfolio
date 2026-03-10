from flask import Flask, render_template, send_from_directory, Response

app = Flask(__name__)

projects = [
    {
        "name": "Jeu Solitaire",
        "description": "Développement d'un jeu de Solitaire complet en Python. Logique de jeu, gestion des états et interface utilisateur.",
        "tech": ["Python"],
        "github": "https://github.com/mart55555/Jeu-Solitaire",
        "icon": "🃏",
        "color": "#003366"
    },
    {
        "name": "Analyse JO 2024",
        "description": "Analyse approfondie des données des Jeux Olympiques de Paris 2024 avec PL/SQL. Requêtes complexes, agrégations et visualisation des performances.",
        "tech": ["PL/SQL", "Oracle DB"],
        "github": "https://github.com/mart55555/Analyse-des-donnes-des-JO-2024",
        "icon": "🏅",
        "color": "#9E1B32"
    },
    {
        "name": "Bibliothèque de jeux vidéo",
        "description": "Développement d'une application web complète en PHP. Gestion de bases de données et interface responsive.",
        "tech": ["PHP", "HTML", "CSS", "MySQL"],
        "github": "https://github.com/mart55555/Developpement-application-php",
        "icon": "🌐",
        "color": "#003366"
    },
    {
        "name": "Power BI Sales Analysis",
        "description": "Dashboard Power BI d'analyse des ventes. Visualisations interactives, KPIs et rapports dynamiques pour la prise de décision.",
        "tech": ["Power BI", "DAX"],
        "github": "https://github.com/mart55555/Power-bi-sales-analysis-",
        "icon": "📊",
        "color": "#9E1B32"
    },
    {
        "name": "RestoN",
        "description": "Application de gestion de restaurant en PHP. Gestion des commandes, menus, réservations et interface d'administration.",
        "tech": ["PHP", "HTML", "CSS", "MySQL"],
        "github": "https://github.com/mart55555/RestoN",
        "icon": "🍽️",
        "color": "#003366"
    }
]

activities = [
    {
        "title": "Data Analysis",
        "icon": "📈",
        "description": "Passionné par l'analyse de données, je transforme des jeux de données brutes en insights actionnables. Maîtrise de SQL, Power BI et des techniques statistiques.",
        "skills": ["Power BI", "SQL", "Excel avancé", "Visualisation"]
    },
    {
        "title": "Cybersécurité",
        "icon": "🔐",
        "description": "Intérêt fort pour la sécurité des systèmes d'information. Étude des protocoles de sécurité, des vulnérabilités et des bonnes pratiques HTTPS/réseau.",
        "skills": ["Network Security", "HTTPS", "Protocoles", "Audit"]
    },
    {
        "title": "Développement Web",
        "icon": "💻",
        "description": "Développement full-stack avec une appétence pour les architectures propres. De la conception à la mise en production.",
        "skills": ["PHP", "Python", "Flask", "MySQL"]
    },
    {
        "title": "Veille Technologique",
        "icon": "🔭",
        "description": "Curieux de nature, je suis en permanence les évolutions du secteur tech : IA, cloud computing, nouvelles architectures et tendances du marché.",
        "skills": ["IA/ML", "Cloud", "Architecture", "Tendances"]
    }
]

@app.route('/')
def home():
    recent = [projects[4], projects[3], projects[2]]
    return render_template('index.html', projects=recent)

@app.route('/projets')
def projets_view():
    all_projects = list(projects)
    return render_template('projets.html', projects=all_projects)

@app.route('/Profil')
def activites_view():
    return render_template('Moi.html', activities=activities)

@app.route('/robots')
def robots():
    content = """User-agent: *
Allow: /
Sitemap: https://adrienmartin.vercel.app/sitemap.xml"""
    return Response(content, mimetype='text/plain')


# ---- Sitemap avec TES vraies pages ----
@app.route('/sitemap.xml')
def sitemap():
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://adrienmartin.vercel.app/</loc>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://adrienmartin.vercel.app/projets</loc>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://adrienmartin.vercel.app/Profil</loc>
        <priority>0.8</priority>
    </url>
</urlset>'''
    return Response(xml, mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)
