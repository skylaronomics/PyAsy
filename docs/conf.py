#
# PyWENO documentation build configuration file
#

import sys, os

# path to autogen'ed modules
sys.path.append(os.path.abspath('..'))

# extentions
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.pngmath']

# general configuration
source_suffix  = '.rst'
master_doc     = 'index'

# html configuration
pygments_style = 'sphinx'
html_theme     = 'default'

# project information
project   = 'PyAsy'
copyright = '2009, Matthew Emmett'

execfile('../version.py')               # this sets 'version'
release = version
