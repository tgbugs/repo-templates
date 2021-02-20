import re
from setuptools import setup


def find_version(filename):
    _version_re = re.compile(r"__version__ = ['\"](.*)['\"]")
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)


__version__ = find_version('{:MODULE_NAME}/__init__.py')

with open('README.org', 'rt') as f:
    long_description = f.read()

tests_require = ['pytest']

setup(name='{:PROJECT_NAME}',
      version=__version__,
      description='',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/{:GROUP_NAME}/{:REPO_NAME}',
      author='{:AUTHOR_NAME}',
      author_email='{:AUTHOR_EMAIL}',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      keywords=('python'),
      packages=[
          '{:MODULE_NAME}',
      ],
      python_requires='>=3.7',
      tests_require=tests_require,
      install_requires=[
      ],
      extras_require={'test': tests_require,
                     },
      scripts=[],
      entry_points={'console_scripts': [ ],},
     )
