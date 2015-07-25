import sys

import requests.certs
from cx_Freeze import Executable, setup

'''
To compile type "py -3 setup.py build_exe" in comand prompt
'''

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Генератор заданий',
    version='1.0.0',
    description='',

    options={
        'build_exe': {
            'optimize': 2,
            'include_msvcr': True,
            'packages': ['os', 'sys', 'json', 'copy', 're', 'random'],
            'includes': ['re', 'PyQt4.QtCore', 'PyQt4.uic', 'PyQt4.Qt', 'PyQt4.QtGui'],
            'excludes': ['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            'include_files': [
                'tools',
                # to importing requests for freezing app
                (requests.certs.where(), 'cacert.pem')
            ],
            'silent': True,
        }
    },

    executables=[
        Executable(
            targetName='Task Generator.exe',
            script='main.pyw',
            excludes=['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            compress=True,
            icon='tools\main.ico',
            base=base
        )
    ]
)
