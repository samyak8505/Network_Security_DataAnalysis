from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This func wwill return the list of requirements
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines() ##Read lines from the file
            for line in lines:
                ##Process each line
                requirement=line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")   

    return requirement_list    

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Samyak Dugad",
    author_email="samyak0805@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

