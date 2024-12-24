from setuptools import setup, find_packages

# Read requirements from requirements.txt
def read_requirements():
    with open("requirements.txt", "r") as f:
        return f.read().splitlines()

setup(
    name="python-analyst-utils",  # Replace with your package name
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
    install_requires=read_requirements(),  # Dynamically load from requirements.txt
)

