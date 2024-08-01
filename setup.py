from setuptools import setup, find_packages

setup(
    name="update_founder",
    version="0.1.0",
    author="Pytholearn-HAZARD(ilia alizade)",
    author_email="police123456789ilia@gmail.com",
    description="A Python package for automatic updating tools.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Pytholearn/update_founder",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)