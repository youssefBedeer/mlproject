from setuptools import setup, find_packages
from typing import List 

def get_requirements(file_path:str) -> List[str]:
    """returns list of requirements"""
    requirements = []
    HYPHEN_E = "-e ."
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
    if HYPHEN_E in requirements:
        requirements.remove(HYPHEN_E)
    return requirements

setup(
    name= "mlproject",
    version= "0.0.1",
    author= "Youssef Bedeer",
    author_email= "yousser1bedeer@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)