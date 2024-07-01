# test_judge.py
import unittest
from judge import judge_code

class TestCodeJudge(unittest.TestCase):
    def test_ruby_code(self):
        code = 'puts "Hello, Ruby!"'
        output, error = judge_code("ruby", code)
        self.assertEqual(output.strip(), "Hello, Ruby!")
        self.assertEqual(error, "")

    def test_go_code(self):
        code = 'package main\nimport "fmt"\nfunc main() {\nfmt.Println("Hello, Go!")\n}'
        output, error = judge_code("go", code)
        self.assertEqual(output.strip(), "Hello, Go!")
        self.assertEqual(error, "")

    def test_rust_code(self):
        code = 'fn main() {\nprintln!("Hello, Rust!");\n}'
        output, error = judge_code("rust", code)
        self.assertEqual(output.strip(), "Hello, Rust!")
        self.assertEqual(error, "")

if __name__ == '__main__':
    unittest.main()
