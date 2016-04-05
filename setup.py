"""
cryptoconditions provide a mechanism to describe a signed
message such that multiple actors in a distributed system
can all verify the same signed message and agree on whether
it matches the description.
"""

from setuptools import setup, find_packages

tests_require = [
    'pytest',
    'coverage',
    'pep8',
    'pyflakes',
    'pylint',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
]

dev_require = [
    'ipdb',
    'ipython',
]

docs_require = [
    'recommonmark>=0.4.0',
    'Sphinx>=1.3.5',
    'sphinxcontrib-napoleon>=0.4.4',
    'sphinx-rtd-theme>=0.1.9',
]

setup(
    name='cryptoconditions',
    version='0.1.2',
    description='cryptoconditions provide a mechanism to describe a signed '
                'message such that multiple actors in a distributed system '
                'can all verify the same signed message and agree on whether '
                'it matches the description.',
    long_description=__doc__,
    url='https://github.com/bigchaindb/cryptoconditions/',
    author='Cryptoconditions Contributors',
    author_email='dev@bigchaindb.com',
    license='MIT',
    zip_safe=True,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
    ],

    packages=find_packages(exclude=['tests*']),

    install_requires=[
        'pysha3==0.3',
        'cryptography==1.2.1',
        'base58==0.2.2',
        'bitcoin==1.1.42',
        'ed25519',
    ],
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'dev':  dev_require + tests_require + docs_require,
        'docs':  docs_require,
    },
)
