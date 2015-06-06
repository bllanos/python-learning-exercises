"""A skeleton project

Additional resources consulted:
- https://github.com/pypa/sampleproject
- https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages

test_requires = [
    'nose'
    ]
    
config = {
    'description': 'Skeleton project',
    'author': 'various',
    'author_email':'various',
    'url': 'none',
    'version': '0.1.0',
    'extras_require': {
        'test': test_requires # As seen here: https://github.com/pypa/sampleproject/blob/master/setup.py
    },
    # For use with `python setup.py test`,
    # as seen here: http://stackoverflow.com/questions/15422527/best-practices-how-do-you-list-required-dependencies-in-your-setup-py?lq=1
    'tests_require': test_requires,
    'packages': find_packages(exclude=['tests*']),
    'name': 'skeleton',
    'entry_points': {
        'console_scripts': [
            'skeleton=skeleton:main'
        ],
    },
}

setup(**config)
