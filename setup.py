from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT= "-e ."

def get_requirements(file_path:str)->List[str]:
    # This fucntion will return the list of requirements

    requirements = []

    with open(file_path) as file_obj:
        requirements = [
            req.strip()
            for req in file_obj.readlines()
            if req.strip() and req.strip() != HYPHEN_E_DOT
        ]

    return requirements



setup(
    name = "ML Project",
    version = "0.0.1",
    author = "Himangi",
    author_email = "himangiisngh2209@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt'),
                        
)