import subprocess
import sys

NOTEBOOK_NAME = "XPINN_for_Buckley_Leverett.ipynb"

def run_notebook():
    try:
        print("Executing notebook...")

        subprocess.run([
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            NOTEBOOK_NAME
        ], check=True)

        print("Notebook executed successfully.")

    except subprocess.CalledProcessError as e:
        print("Error: Notebook execution failed.")
        print(e)
    except FileNotFoundError:
        print("Error: Jupyter is not installed. Install it using:")
        print("pip install jupyter")

if __name__ == "__main__":
    run_notebook()
