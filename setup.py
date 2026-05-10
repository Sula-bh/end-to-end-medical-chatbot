from setuptools import find_packages, setup

setup(
    name="med-chatbot",
    version="0.0.1",
    author="Sulabh Acharya",
    author_email="sulava06@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
