from setuptools import setup, find_packages

print(f"Found packages: {find_packages()}")

setup(
    name='splitter',
    packages=find_packages(),
    description='Tool for K-Fold Stratification',
    version='0.1',
    url='',
    author='Philipp Sodmann',
    author_email='psodmann@gmail.com',
    keywords=['Pytorch', "Splitting"]
)
