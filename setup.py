from setuptools import setup, find_packages

setup(
   name='FighterGame',
   version='0.0.1',
   author='Mael Babert',
   author_email='babert-m@saint-louis29.net',
   license='LICENSE.txt',
   description='An awesome fighter game',
   long_description=open('README.md').read(),
   install_requires=[
       "pytest",
       "pillow",
   ],

    packages=find_packages(
        where='src',
    ),
    package_dir={"": "src"}

)
