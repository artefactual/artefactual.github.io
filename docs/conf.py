# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Contributors Portal'
copyright = '2024, Artefactual'
author = 'Artefactual'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

html_logo = "_static/img/logo-toolbox.png"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']


html_title = "Contributors Portal"

html_theme_options = {
    "source_repository": "https://github.com/artefactual/artefactual.github.io/",
    "source_branch": "main",
    "source_directory": "docs/",
}
