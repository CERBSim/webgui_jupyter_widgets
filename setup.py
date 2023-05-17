#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified LGPLv2.1 License.

from __future__ import print_function
from glob import glob
import os, json
from os.path import join as pjoin
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
import shutil


from jupyter_packaging import (
    create_cmdclass,
    install_npm,
    ensure_targets,
    combine_commands,
    get_version,
)

HERE = os.path.dirname(os.path.abspath(__file__))




# The name of the project
name = 'webgui_jupyter_widgets'

# Get the version
version = json.load(open('package.json'))['version']

webgui_dir = os.path.join(HERE,"webgui")
webgui_version = json.load(open('webgui/package.json'))['version']


# Representative files that should exist after a successful build
jstargets = [
    pjoin(HERE, name, 'nbextension', 'index.js'),
    pjoin(HERE, 'lib', 'plugin.js'),
]


package_data_spec = {
    name: [
        'nbextension/**js*',
        'labextension/**',
        'js/**'
    ]
}


data_files_spec = [
#    ('share/jupyter/nbconvert/templates/webgui', 'template', '**'),
    ('share/jupyter/nbextensions/webgui_jupyter_widgets', 'webgui_jupyter_widgets/nbextension', '**'),
    ('share/jupyter/labextensions/webgui_jupyter_widgets', 'webgui_jupyter_widgets/labextension', '**'),
    ('share/jupyter/labextensions/webgui_jupyter_widgets', '.', 'install.json'),
    ('etc/jupyter/nbconfig/notebook.d', '.', 'webgui_jupyter_widgets.json'),
]

class generate_webgui_js(build_ext):
    def run(self):
        webgui_js_code = open(os.path.join(webgui_dir, 'dist','webgui.js')).read()
        open('webgui_jupyter_widgets/webgui_js.py','w').write(
"""version = "{}"
code = r\"\"\"{}\"\"\"

if __name__ == '__main__':
    import sys
    open(sys.argv[1], 'w').write(code)
""".format(webgui_version, webgui_js_code))

#        open('template/index.html.j2','w').write(
#"""{%- extends 'classic/index.html.j2' -%}
#
#{%- block html_head_js -%}
#  {{ super() }}
#  <script>
#{{{webgui_code}}}
#
#  </script>
#{%- endblock html_head_js -%}
#""".replace("{{{webgui_code}}}", webgui_js_code))
        join = os.path.join
        js_dir = join(HERE, 'webgui_jupyter_widgets', 'js')
        shutil.copy( join(webgui_dir,'dist','webgui.js'), js_dir)
        shutil.copy( join(HERE, 'dist', 'index.js'), join(js_dir, 'webgui_jupyter_widgets.js'))

is_dev_build = bool(os.environ.get('DEV_BUILD', False))
cmdclass = create_cmdclass('jsdeps', package_data_spec=package_data_spec,
    data_files_spec=data_files_spec)
cmdclass['jsdeps'] = combine_commands(
    install_npm(webgui_dir, build_cmd='build' if not is_dev_build else 'build-dev'),
    install_npm(HERE, build_cmd='build:prod' if not is_dev_build else 'build'),
    ensure_targets(jstargets),
    generate_webgui_js,
)


setup_args = dict(
    name            = name,
    description     = 'Jupyter widgets library for webgui js visualization library',
    version         = version,
    scripts         = glob(pjoin('scripts', '*')),
    cmdclass        = cmdclass,
    packages        = find_packages(),
    package_dir     = {"webgui_jupyter_widgets": "webgui_jupyter_widgets"},
    author          = 'CERBSim',
    author_email    = 'mhochsteger@cerbsim.com',
    url             = 'https://github.com/CERBSim/webgui_jupyter_widgets',
    license_files   = ['LGPLv2.1'],
    platforms       = "Linux, Mac OS X, Windows",
    keywords        = ['Jupyter', 'Widgets', 'IPython'],
    classifiers     = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Jupyter',
    ],
    include_package_data = True,
    python_requires=">=3.6",
    install_requires = [
        'ipywidgets>=7.0.0',
    ],
    extras_require = {
        'test': [
            'pytest>=4.6',
            'pytest-cov',
            'nbval',
        ],
        'examples': [
            # Any requirements for the examples to run
        ],
        'docs': [
            'jupyter_sphinx',
            'nbsphinx',
            'nbsphinx-link',
            'pytest_check_links',
            'pypandoc',
            'recommonmark',
            'sphinx>=1.5',
            'sphinx_rtd_theme',
        ],
    },
    entry_points = {
    },
)

if __name__ == '__main__':
    setup(**setup_args)
