# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Average Squares'
copyright = '2025, Sam Holt'
author = 'Sam Holt'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

# Ensure the project root is on sys.path so Sphinx can import the package/module.
# From docs/conf.py, the project root is one directory up.
sys.path.insert(0, os.path.abspath('..'))

extensions = ['sphinx.ext.autodoc']

# Common autodoc options so `automodule`/`autoclass` include members by default.
autodoc_default_options = {
	'members': True,
	'undoc-members': True,
	'show-inheritance': True,
}

autoclass_content = 'both'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
