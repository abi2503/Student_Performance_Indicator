#This is required to use our ML application as packages
from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function reads the required packages from requirements.txt
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name='Student_Performance_Indicator',
    version='0.0.1',
    author='Abhishek Suresh',
    author_email='as18757@nyu.edu',
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )