# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'My5.tv/activate'
copyright = '2025, My5'
author = 'My5 Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (optional)
# html_theme = 'sphinx_rtd_theme'

# ✅ SEO-Optimized Titles Using Your Keyword
html_title = "My5.tv/activate – Easy Guide to Activate My5 on Any Device"
html_short_title = "My5 Activation Guide"

# ✅ Optional: Add Meta Keywords for SEO
html_meta = {
    "description": "Visit My5.tv/activate to activate My5 on Smart TV, Firestick, Roku & more. Step-by-step activation guide with troubleshooting.",
    "keywords": "My5.tv/activate, Activate My5, My5 activation, My5 on Smart TV, My5 Firestick, My5 Roku"
}

# Favicon
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files (for buttons)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets
# html_static_path = ['_static']
