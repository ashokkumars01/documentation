import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information
project = 'MyProject'
version = ''  # short version
release = ''  # full version

# -- General configuration
extensions = [
    'sphinx_rtd_theme',
    'sphinx_multiversion',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- sphinx-multiversion config
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'  # only tags like v1.0.0
smv_branch_whitelist = r'^master$'
smv_remote_whitelist = r'^origin$'
