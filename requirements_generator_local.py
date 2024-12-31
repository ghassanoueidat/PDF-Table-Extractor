
# requirements_generator.py

import os

def generate_requirements():
    requirements = [
        "camelot-py[cv]",
        "pandas",
        "openpyxl",
        "matplotlib",
        "PyPDF2==1.26.0",
        "tkinter"
    ]
    
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'requirements.txt')
    
    with open(file_path, 'w') as file:
        file.write('\n'.join(requirements))
    
    print(f"requirements.txt generated successfully at {file_path}")


if __name__ == '__main__':
    generate_requirements()
