from setuptools import setup, find_packages

dependencies = [
    # Basic dependencies
    'requests',

    # Testing dependencies
    'nose',
    'coverage',
    'coveralls',
    'httmock'
]

setup(
    name="nhtsa",
    version="0.1.0",
    author="Evan Darwin",
    author_email="evan@relta.net",
    description="A library for accessing the NHTSA API",
    license="proprietary",
    keywords="international domain library",
    url="https://github.com/EvanDarwin/NHTSA-python",
    packages=find_packages(exclude=['tests']),
    install_requires=dependencies,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
)