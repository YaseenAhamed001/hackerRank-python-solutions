"""
create_repo_structure.py

This script automatically generates a structured HackerRank solutions repository.
It creates folders and files according to a pre-defined structure:
Usage:
    python create_repo_structure.py [target_directory]

If no target_directory is provided, it uses the current working directory.
"""

import os
import sys


STRUCTURE = {
    "README.md": "",
    "requirements.txt": "# Add dependencies here if required\n",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n",
    "docs": {
        "index.md": "# Documentation\n"
    },
    "problems": {
        "algorithms": {},
        "data_structures": {},
        "sql": {},
        "python": {},
        "C++": {}
    },
    "scripts": {
        "run_solution.py": ""
    }
}


def create_structure(base_path, structure):
    """
    Recursively creates directories and files based on the STRUCTURE dictionary.

    Args:
        base_path (str): The directory where the structure should be created.
        structure (dict): A dictionary where keys are file/folder names and values are:
            - dict → a nested folder
            - str → file content
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            if os.path.exists(path) and name == "create_repo_structure.py":
                continue
            with open(path, "w", encoding="utf-8") as file:
                file.write(content)




def main():
    """
    Entry point of the script.
    """
    # Use current directory or the path passed in CMD
    base_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    # Directly create files/folders in base_path, no extra folder
    create_structure(base_path, STRUCTURE)

    print(f"Repository structure created inside:\n{base_path}")


if __name__ == "__main__":
    main()

# python create_repo_structure.py
