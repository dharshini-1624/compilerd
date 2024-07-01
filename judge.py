from go_compiler import compile_and_run_go
from rust_compiler import compile_and_run_rust

def judge_code(language, code):
    if language == "python":
        # existing code
        pass
    elif language == "ruby":
        return compile_and_run_ruby(code)
    elif language == "go":
        return compile_and_run_go(code)
    elif language == "rust":
        return compile_and_run_rust(code)

