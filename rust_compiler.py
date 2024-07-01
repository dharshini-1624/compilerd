# rust_compiler.py
import subprocess

def compile_and_run_rust(code):
    with open("main.rs", "w") as f:
        f.write(code)
    
    subprocess.run(["rustc", "main.rs"])
    result = subprocess.run(["./main"], capture_output=True, text=True)
    return result.stdout, result.stderr
