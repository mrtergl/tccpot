from setuptools import setup


def readme_file_contents():
    with open('README.rst') as readme_file:
        data = readme_file.read()
    return data


setup(
    name="tcppot",
    version="1.0.0",
    description="Simple TCP tcppot",
    long_description=readme_file_contents(),
    author="Murat Ergul",
    license="MIT",
    packages=["tcppot"],
    zip_safe=False,
    install_requires=[
        'docopt'
    ]
)
