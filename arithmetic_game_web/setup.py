from setuptools import setup, find_packages
    
config = {
    'description': 'Simple online arithmetic game, created for Learning Python the Hard Way, Exercise 52',
    'author': 'bllanos',
    'url': 'none',
    'version': '0.1.0',
    'install_requires': ['web.py'],
    # To run tests: `python setup.py nosetests`
    # See http://nose.readthedocs.org/en/latest/api/commands.html
    'setup_requires':[
        'nose>=1.0',
        'coverage>=3.7'
    ],
    'packages': find_packages(exclude=['tests*']),
    'name': 'arithmetic_game_web',
    'entry_points': {},
}

setup(**config)
