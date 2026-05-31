# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from datetime import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Avion Coast'
copyright = '2025 - 2026, Kate Redfern'
author = 'Kate Redfern'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

today = '%Y-%b-%d'

extensions = ['sphinx_rtd_theme', 'myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'prev_next_buttons_location': 'both',
    'style_nav_header_background': '#DF0000'
    }

# -- Options for Markup ------------------------------------------------------
# https://www.shinx-doc.org/en/master/usage/configuration.html#options-for-markup

rst_prolog = """
.. |last_session| replace:: May 17th, 2026
.. |next_session| replace:: May 31st, 2026
"""
