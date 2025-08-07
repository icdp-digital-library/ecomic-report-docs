# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Ecomic - Ecosistema digitale per la cultura'
copyright = '2025, Istituto centrale per la digitalizzazione del patrimonio culturale - Digital Library'
author = 'Digital Library'
release = '1.0'
version = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode', 
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'it'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Configurazioni tema Read the Docs ottimizzate per Docs Italia
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#0066CC',  # Colore blu PA
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Metadati per Docs Italia
html_context = {
    'display_github': True,
    'github_user': 'icdp-digital-library',
    'github_repo': 'ecomic-report-docs',  # SOSTITUISCI con il nome effettivo del tuo repo
    'github_version': 'main',
    'conf_py_path': '/source/',
    'last_updated': True,
    'commit': False,
}

# CSS personalizzato
html_css_files = [
    'custom.css',
]

# Configurazioni aggiuntive per documenti PA
html_title = f"{project} v{version}"
html_short_title = "Ecomic"

# Logo (se hai un logo da aggiungere)
# html_logo = '_static/logo.png'

# Favicon (se hai un favicon)
# html_favicon = '_static/favicon.ico'

# Numerazione automatica delle figure e tabelle
numfig = True
numfig_format = {
    'figure': 'Figura %s',
    'table': 'Tabella %s',
    'code-block': 'Listato %s'
}

# Configurazioni per PDF
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r'''
\usepackage[utf8]{inputenc}
\usepackage[italian]{babel}
''',
}

latex_documents = [
    ('index', 'ecomic.tex', 'Ecomic - Ecosistema digitale per la cultura',
     'Digital Library', 'manual'),
]

# Configurazioni specifiche per Docs Italia
html_show_sourcelink = True
html_show_sphinx = False