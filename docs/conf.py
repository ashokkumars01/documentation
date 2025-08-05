import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Your Project'
author = 'Your Name'
release = '1.0.0'

extensions = [
    'sphinx_rtd_theme',
    'sphinx_multiversion',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Sphinx-multiversion config
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^master$'
smv_remote_whitelist = r'^origin$'
