import io
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="oca-github-bot",
    use_scm_version=True,
    long_description=long_description,
    author="Odoo Community Association (OCA)",
    author_email="info@odoo-community.org",
    url="https://github.com/OCA/oca-github-bot",
    python_requires=">=3.6",
    setup_requires=["setuptools_scm"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        # aiohttp ang gitgethub for the webhook app
        "aiohttp",
        "gidgethub",
        "appdirs",
        # GitHub client
        "github3.py>=1.3.0",
        # celery and celery monitoring for the task queue
        "flower",
        "celery[redis]",
        # Odoo
        "odoorpc",
        # Sentry
        "raven",
        # setuptools and twine to build, check and upload wheels
        "setuptools",
        "twine",
        "wheel",
        # setuptools-odoo so setup.py bdist_wheel does not need
        # to re-download it for each and every build
        "setuptools-odoo>=3.0.3",
        "lxml",
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
            "pytest-mock",
            "pytest-vcr",
        ],
    },
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
