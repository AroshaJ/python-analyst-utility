from setuptools import setup, find_packages

setup(
    name="python-analyst-utility",
    version="0.1.0",
    author="Rosh Jayawardena",
    author_email="rosh.jayawardena@gmail.com",
    description="A utility package for analysts with Pandas, Excel, CSV helpers and more.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AroshaJ/python-analyst-utility",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "certifi>=2024.12.14",
        "charset-normalizer>=3.4.0",
        "et_xmlfile>=2.0.0",
        "idna>=3.10",
        "numpy>=2.2.1",
        "openpyxl>=3.1.5",
        "packaging>=24.2",
        "pandas>=2.2.3",
        "python-dateutil>=2.9.0.post0",
        "pytz>=2024.2",
        "requests>=2.32.3",
        "urllib3>=2.3.0",
        "xlwings>=0.33.5",
    ],
    extras_require={
        "dev": [
            "pytest>=8.3.4",
            "pytest-mock>=3.14.0",
            "twine>=6.0.1",
            "readme_renderer>=44.0",
            "pkginfo>=1.12.0",
            "keyring>=25.5.0",
            "rich>=13.9.4",
        ],
    },
)


