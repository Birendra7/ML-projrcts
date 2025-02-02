from setuptools import find_packages, setup

HYPRN_E_DOT = '-e .'

def get_requirement(file_path:str)->list[str]:
    
    ''' this function will reaturn the list of equirements
    '''
    requirements=[]
    with open(file_path) as file_obje:
        requirements= file_obje.readlines()
        requirements=  [req.replace("\n","") for req in requirements ]
        
        if HYPRN_E_DOT in requirements:
            requirements.remove(HYPRN_E_DOT)
        
    return requirements
        

setup(
    
    name="mlproject",
    version="0.0.1",
    author="Birendra",
    author_email= "birendraraaz620@gmail.com",
    packages=find_packages(),
    install_require=get_requirement('requirements.txt')
)