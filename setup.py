import re
import setuptools
import sys

with open('README.md') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="queenbee_pollination",
    use_scm_version = True,
    setup_requires=['setuptools_scm'],
    author="Ladybug Tools",
    author_email="info@ladybug.tools",
    description="queenbee-pollination extends queenbee classes to be translatable to Argo workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pollination/queenbee-argo",
    packages=setuptools.find_packages(exclude=["tests", "hack", "docs"]),
    install_requires=requirements,
    extras_require={
        'cli': ['click>=7.0', 'click_plugins==1.1.1']
    },
    entry_points='''
        [queenbee.plugins]
        pollination=queenbee_pollination.cli:pollination
    ''',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent"
    ],
)
