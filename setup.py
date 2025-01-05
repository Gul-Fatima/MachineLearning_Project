from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path : str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #read each line(package) in req.txt and add to list
        requirements = [req.replace ("\n","")for req in requirements] # to remove /n added by default from list while reading req.txt
         
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name = 'mlproject',
    version ='0.0.1',
    author = 'Gul Fatima',
    author_email = 'gulfatima1074@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)