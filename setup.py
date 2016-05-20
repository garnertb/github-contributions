from distutils.core import setup

setup(
    name='github-contributions',
    version='1.1.0',
    packages=['github_contributions'],
    url='https://github.com/garnertb/github-contributions',
    license='GNU General Public License',
    author='Tyler Garner',
    author_email='garnertb@prominentedge.com',
    description='Scrape Github for a user\'s public contributions.',
    install_requires=[
        'requests==2.9.1',
        'bs4==0.0.1',
        'click==6.6'
    ],
    entry_points={
        'console_scripts': [
            'contributions = github_contributions.cli:get_contributions_cli',
        ],
    }
)
