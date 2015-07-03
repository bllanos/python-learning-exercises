from setuptools import setup, find_packages
    
config = {
    'description': 'Learn Python the Hard Way, Exercise 51',
    'author': 'various',
    'author_email':'various',
    'url': 'none',
    'version': '0.1.0',
    'install_requires': ['lpthw.web'],
    # To run tests: `python setup.py nosetests`
    # See http://nose.readthedocs.org/en/latest/api/commands.html
    'setup_requires':[
        'nose>=1.0',
        'coverage>=3.7'
    ],
    'packages': find_packages(exclude=['tests*']),
    'name': 'ex51',
    'entry_points': {},
}

setup(**config)
