import os

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='pelican-render-math',
    version='0.1.1',
    description='Pelican plugin to easy math rendering',
    long_description=readme,
    url='https://github.com/cprieto/pelican-math-render',
    license='MIT',
    author='',
    author_email='',
    py_modules=['render_math'],
    requires=['pelican'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
