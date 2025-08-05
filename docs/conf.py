import os
import sys
sys.path.insert(0, os.path.abspath('.'))

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_multiversion',
    'sphinx_panels',
]
templates_path = ['_templates']
html_theme = "sphinx_rtd_theme"
exclude_patterns = []
html_static_path = ['_static']

# Sphinx-multiversion config
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'   # tags like v1.0.0
smv_branch_whitelist = r'^master$'          # latest from main branch
smv_remote_whitelist = r'^origin$'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
