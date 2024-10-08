import subprocess
import sys

def run_mypy():
    result = subprocess.run(["poetry", "run", "mypy", "static_python_template"], check=False)
    return result.returncode

def run_fastapi():
    subprocess.run(["fastapi", "dev", "static_python_template/app.py"])

def main():
    if run_mypy() == 0:
        run_fastapi()
    else:
        print("Type checking failed. Please fix the errors.")
        sys.exit(1)