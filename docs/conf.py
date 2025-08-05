import os

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 4,
}
extensions = [
    'sphinx_multiversion',
]

# Optional: Use this to skip unwanted tags/branches
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^master$'
smv_remote_whitelist = r'^origin$'
