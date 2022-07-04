# -*- coding: utf-8 -*-
#
# Recommonmark documentation build configuration file, created by
# sphinx-quickstart on Tue Jul 28 11:17:27 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
#
# To build the documentation locally, activate ivadomed venv, then run:
#   make html

import sys
import os
import importlib

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../ivadomed/'))


# TODO: find a way to minimize the number of imports below (maybe by adding
# "import *" in the __init__ files).
import ivadomed


source_suffix = '.rst'

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# -- Extensions to the  Napoleon GoogleDocstring class ---------------------

from sphinx.ext.napoleon.docstring import GoogleDocstring

# first, we define new methods for any new sections and add them to the class
def parse_keys_section(self, section):
    return self._format_fields('Keys', self._consume_fields())
GoogleDocstring._parse_keys_section = parse_keys_section


def parse_attributes_section(self, section):
    return self._format_fields('Attributes', self._consume_fields())


GoogleDocstring._parse_attributes_section = parse_attributes_section


def parse_class_attributes_section(self, section):
    return self._format_fields('Class Attributes', self._consume_fields())


GoogleDocstring._parse_class_attributes_section = parse_class_attributes_section


# we now patch the parse method to guarantee that the the above methods are
# assigned to the _section dict
def patched_parse(self):
    self._sections['keys'] = self._parse_keys_section
    self._sections['class attributes'] = self._parse_class_attributes_section
    self._unpatched_parse()


GoogleDocstring._unpatched_parse = GoogleDocstring._parse
GoogleDocstring._parse = patched_parse


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx-jsonschema',
    'sphinx_tabs.tabs',
    'sphinx_toolbox.collapse',
    'sphinx_copybutton'
]

autoclass_content = "both"
add_module_names = True
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth >= 2
autodoc_default_options = {
    'members': None,
    'member-order': 'bysource',  # 'alphabetical'
    'special-members': None,  # can list e.g. __init__
    'show-inheritance': True,
    # 'undoc-members': True,  # members without docstrings
    'exclude-members': '__weakref__'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'ivadomed'
copyright = u'2020, Ivadomed team'
author = u'Ivadomed team'

github_doc_root = 'https://github.com/neuropoly/ivadomed/tree/master/docs/'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# TODO: uncomment once ivadomed can be imported
version = ivadomed.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If false. removes the module names for functions (e.g., ivadomed.module.function becomes function)
add_module_names = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "collapse_navigation": True,
    "display_version": True,
    "sticky_navigation": True,  # Set to False to disable the sticky nav while scrolling.
    "logo_only": True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    "style_nav_header_background": "#FBFBFB",
}

html_context = {
    "display_github": True,
    "github_user": "neuropoly",
    "github_repo": "ivadomed",
    "github_version": "master",
    "conf_py_path": "/docs/",
}

html_scaled_image_link = False
html_show_sourcelink = True

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Home"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "../../images/ivadomed_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['css/custom.css']
# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = False

smart_quotes = False
# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'ivadomed-doc'


# PATCH `sphinx-jsonschema`
#  to render the extra `options`` and ``tags`` schema properties
#
def _patched_sphinx_jsonschema_simpletype(self, schema):
    """Render the *extra* ``required`` and ``options`` schema properties for every object."""
    rows = _original_sphinx_jsonschema_simpletype(self, schema)

    if "required" in schema:
        required = schema["required"]
        if required not in ["true", "false"]:
            raise Exception("The required argument must be one of true, false")
        rows.append(self._line(self._cell("required"), self._cell(required)))
        del schema["required"]

    if "range" in schema:
        range = schema["range"]
        rows.append(self._line(self._cell("range"), self._cell(range)))
        del schema["range"]

    # if "options" in schema:
    #     rows.append(self._line(self._cell("options"), self._cell("")))
    #     for option in schema["options"]:
    #         rows.append(self._line(self._cell(""), self._cell(f"``{option}``"), self._cell("test")))
    #
    #     del schema["options"]

    if "options" in schema:
        key = "options"
        rows.append(self._line(self._cell(key)))

        for prop in schema[key].keys():
            # insert spaces around the regexp OR operator
            # allowing the regexp to be split over multiple lines.
            # proplist = prop.split('|')
            # dispprop = self._escape(' | '.join(proplist))
            dispprop = prop
            bold = '``'
            label = self._cell(bold + dispprop + bold)

            if isinstance(schema[key][prop], dict):
                obj = schema[key][prop]
                rows.extend(self._dispatch(obj, label)[0])
            else:
                rows.append(self._line(label, self._cell(schema[key][prop])))
        del schema[key]

    return rows


sjs_wide_format = importlib.import_module("sphinx-jsonschema.wide_format")
_original_sphinx_jsonschema_simpletype = sjs_wide_format.WideFormat._simpletype  # type: ignore
sjs_wide_format.WideFormat._simpletype = _patched_sphinx_jsonschema_simpletype  # type: ignore
