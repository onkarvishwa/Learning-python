import os
import sys

def print_directory_contents(directory_path='.'):
    """
    Lists all files and subdirectories in the specified directory path.
    The default path is '.' (the current working directory).

    It uses the os.listdir() function, which was found via online search,
    to return a list of entry names (files and directories) in the path.
    """
    # Get the absolute path for clear display
    try:
        absolute_path = os.path.abspath(directory_path)
    except Exception:
        # Fallback if abspath fails
        absolute_path = directory_path

    print(f"\n {absolute_path} ---")

    try:
        # Use os.listdir() to get the list of names
        entries = os.listdir(directory_path)

        if not entries:
            print("The directory is empty.")
            return

        print(f"Found {len(entries)} entries:")

        # Sort entries alphabetically before printing
        for entry in sorted(entries):
            # Check the type of entry for better visual feedback
            full_path = os.path.join(directory_path, entry)

            if os.path.isdir(full_path):
                print(f"[DIR]  {entry}")
            elif os.path.isfile(full_path):
                print(f"[FILE] {entry}")
            else:
                print(f"[OTHER] {entry}")

    except FileNotFoundError:
        print(f"ERROR: Directory not found at path: '{directory_path}'")
    except PermissionError:
        print(f"ERROR: Permission denied to access directory: '{directory_path}'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Example Usage ---

# 1. List contents of the current directory (runs when no arguments are provided)
print_directory_contents()

# 2. Optionally, allow a path to be passed as a command-line argument
# To run this, you would execute: python list_directory.py /some/other/path
if len(sys.argv) > 1:
    custom_path = sys.argv[1]
    print("\n" + "="*50)
    print_directory_contents(custom_path)
    print("="*50 + "\n")

# To use this in your environment, save the code as a .py file
# and run it from your terminal.
print(content)