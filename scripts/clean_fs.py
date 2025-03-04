import os
import shutil

def delete_paths():
    # Directories and file to remove
    paths_to_remove = ["tmp_html", "tmp_json", "__pycache__", "public", "resources"]
    file_to_remove = ".hugo_build.lock"
    
    for root, dirs, files in os.walk(os.getcwd(), topdown=True):
        # Remove matching directories
        for d in paths_to_remove:
            dir_path = os.path.join(root, d)
            if os.path.isdir(dir_path):
                print(f"Deleting directory: {dir_path}")
                shutil.rmtree(dir_path, ignore_errors=True)
        
        # Remove matching file
        file_path = os.path.join(root, file_to_remove)
        if os.path.isfile(file_path):
            print(f"Deleting file: {file_path}")
            os.remove(file_path)

if __name__ == "__main__":
    delete_paths()
