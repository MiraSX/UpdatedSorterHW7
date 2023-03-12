from setuptools import setup, find_namespace_packages
import unicodedata 

setup(name='clean_folder',
      author='MiraSX',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:sorting']})

