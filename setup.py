from setuptools import setup, find_packages

setup(
    name="Auto_Update",
    version="2.8.12",
    author="Pytholearn-HAZARD(ilia alizade)",
    author_email="police123456789ilia@gmail.com",
    description="A Python package for automatic updating tools.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pytholearn/Auto_Update",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
