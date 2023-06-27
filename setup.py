from setuptools import find_packages, setup
from typing import List


SETUP_TRIGGER = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    A simple function that takes in a file and feeds it into the setup
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if SETUP_TRIGGER in requirements:
            requirements.remove(SETUP_TRIGGER)

    return requirements

setup(
    name='MLOPs Projects',
    version='0.1',
    description='A project aimed at building multiple ML projects and deploying to the pipeline...',
    author='Isaac Ige',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)