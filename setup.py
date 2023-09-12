from setuptools import setup,find_packages

def get_requirements(filepath):
    requirements = []
    with open(filepath,"r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(
 name = "project02-CICD pipeline",
 version = "0.0.1",
 description="This is a practice project for CI/CD pipeline",
 author="Arifa Mustafa",
 author_email="arifacsdsu@gmail.com",
 packages=find_packages(),
 install_require = get_requirements("requirements.txt")
)