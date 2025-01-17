import os
from typing import List, Tuple

def create_files(folder_path: str, files: List[Tuple[str, str]]):
    """
    Create files at the specified folder location with given content.

    Args:
        folder_path (str): The path to the folder where files will be created.
        files (List[Tuple[str, str]]): A list of tuples containing file names and their content.
    """
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    for file_name, content in files:
        file_path = os.path.join(folder_path, file_name)

        # Write content to the file
        if os.path.exists(content):
            with open(content, 'r', encoding='utf-8') as content_file:
                content = content_file.read()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File created: {file_path}")


def read_files_from_text(file_path: str) -> List[Tuple[str, str]]:
    """
    Read file names and content from a text file. The text file should have the format:
    <file_name>::<content>

    Args:
        file_path (str): Path to the text file containing file definitions.

    Returns:
        List[Tuple[str, str]]: A list of tuples with file names and content.
    """
    files = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '::' in line:
                file_name, content = line.strip().split('::', 1)
                files.append((file_name, content))

    return files


def main(folder_location: str = "output_folder", files_name: List[str] = None, files_content: List[str] = None):
    """
    Main function to create files using provided parameters or from a text file.

    Args:
        folder_location (str): Folder where files will be created.
        files_name (List[str], optional): List of file names.
        files_content (List[str], optional): List of file contents corresponding to files_name.
    """
    # Create files from parameters if provided
    if files_name and files_content and len(files_name) == len(files_content):
        files_data = list(zip(files_name, files_content))
        print("Creating files from parameters...")
        create_files(folder_location, files_data)
    else:
        print("Parameters for files_name and files_content are missing or mismatched. Skipping parameter-based file creation.")

    # Example usage with text file input
    text_file_path = "file_definitions.txt"

    print("\nReading file definitions from text file...")
    if os.path.exists(text_file_path):
        files_from_text = read_files_from_text(text_file_path)
        create_files(folder_location, files_from_text)
    else:
        print(f"Text file '{text_file_path}' not found. Skipping this step.")


if __name__ == "__main__":
    main()
