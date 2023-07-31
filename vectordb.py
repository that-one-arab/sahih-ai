import sys
import os

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    # Get the current working directory and append it to sys.path
    current_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(current_path)

    # Read the CLI argument
    if len(sys.argv) < 2:
        print("Usage: python vectordb.py <init | reset>")
    else:
        script_name = sys.argv[1]
        if script_name == 'init':
            import lib.vectordb.init
        elif script_name == 'reset':
            import lib.vectordb.reset