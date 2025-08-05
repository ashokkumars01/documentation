import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'My Documentation'
author = 'Your Name'
release = 'v1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_multiversion',
    'myst_parser',  # Only if using markdown
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Theme
html_theme = 'furo'

# Output directory
html_static_path = ['_static']

# For versioning
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^main$'
smv_remote_whitelist = r'^origin$'
smv_released_pattern = r'^tags/v\d+\.\d+\.\d+$'
smv_latest_version = 'v1.0.0'
