# go_compiler.py
import subprocess

def compile_and_run_go(code):
    with open("main.go", "w") as f:
        f.write(code)
    
    subprocess.run(["go", "build", "main.go"])
    result = subprocess.run(["./main"], capture_output=True, text=True)
    return result.stdout, result.stderr
