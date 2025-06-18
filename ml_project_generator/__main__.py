# Project template generator for ml projects

# Imports: 
import argparse
import os

def build_folder(project_path:str, folder_name:str)->str:
    """ Build and folder using os and returns the path to the folder that was just created"""
    folder_path = os.path.join(project_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    return folder_path

def main():
    parser = argparse.ArgumentParser() # reading inputs from command line

    parser.add_argument("output_path")
    parser.add_argument("project_name")

    args = parser.parse_args() # getting the arguments from the command line

    if not os.path.isdir(args.output_path):
        raise ValueError(f"Output path '{args.output_path}' is not a valid directory.")

    project_path = os.path.join(args.output_path, args.project_name)
    os.makedirs(project_path, exist_ok=True)
    
    data_folder_path = build_folder(project_path, "data")
    _ = build_folder(data_folder_path, "raw") # subfolder to store raw data
    _ = build_folder(data_folder_path, "cleaned") # subfolder to store the processed data

    _ = build_folder(project_path, "notebooks") # folder to store notebooks

    src_folder_path = build_folder(project_path, "src") # folder to store notebooks
    _ = build_folder(src_folder_path, "data") # subfolder to store Data handling and preprocessing
    _ = build_folder(src_folder_path, "models") # subfolder to store models and evaluation

    _ = build_folder(project_path, "tests") # folder to store unitests
    _ = build_folder(project_path, "config") # folder to store config files
    _ = build_folder(project_path, "reports") # folder to store plots and results

    readme_path = os.path.join(project_path, "README.md")
    open(readme_path, "w").close()

    print(f"project has been created at: {project_path}")
