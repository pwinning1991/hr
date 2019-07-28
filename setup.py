from setuptools impot setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Commandline user managment utility',
    long_description=readme,
    author='Philip Winnington',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
