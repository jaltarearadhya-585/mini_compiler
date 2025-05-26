🔧 Mini Compiler for Custom Language (Python-Based)

This project is a **Mini Compiler** built in Python for a custom-designed programming language. It covers all major phases of a compiler including lexical analysis, syntax parsing, semantic analysis, and intermediate code generation (ICG), with a simple graphical user interface (GUI).

## 🧠 Features

- **Lexical Analysis** – Tokenizes the source code.
- **Syntax Analysis (Parser)** – Parses tokens using grammar rules.
- **Semantic Analysis** – Checks for semantic errors and performs type-checking.
- **Intermediate Code Generation (ICG)** – Generates intermediate representation of code.
- **GUI** – Simple Python-based GUI to compile code interactively.
- **Unit Tests** – Included for each major module.

---

## 🗂️ Project Structure
mini_compiler/
├── pycache/ # Python bytecode cache
├── icg.py # Intermediate Code Generation module
├── lexer.py # Lexical Analyzer
├── mini_compiler_gui.py # GUI for the mini compiler
├── my_parser.py # Grammar definition and parser rules
├── parser.out # Generated parser output
├── parser.py # Parser logic
├── parsetab.py # Parsing table (auto-generated)
├── semantic.py # Semantic analysis logic
├── semantic_analyzer.py # Entry point for semantic analysis
├── test_icg.py # Unit tests for ICG
├── test_lexer.py # Unit tests for lexer
├── test_parser.py # Unit tests for parser
├── test_semantic.py # Unit tests for semantic analysis

✅ Run Unit Tests
bash
Copy
Edit
python test_lexer.py
python test_parser.py
python test_semantic.py
python test_icg.py

📌 Requirements
   Python 3.6+
   PLY (Python Lex-Yacc)

   Install dependencies using:
   bash
   Copy
   Edit
   pip install ply


 About the Language
Our custom language supports:
->Variable declarations
->Arithmetic operations
->Conditional statements (if, else)
->Loops (while, for)
->Basic error reporting in semantic analysis

🤝 Contributors
Dhruv Gahtori (B.Tech CSE-team head )
Kamal Joshi (B.Tech CSE )
Aradhya Abhay Jaltare (B.Tech CSE )
Deepesh Singh Kharkwal (B.Tech CSE )

📜 License
This project is for educational purposes. You are free to use and modify it.
