GROUP MEMBERS: Carson Pautz

**Python Grammar Parser with Dynamic Indentation Support**

This project is a Python grammar parser implemented using ANTLR4. It supports dynamic Python-style indentation (INDENT/DEDENT) for parsing Python-like scripts. 
The lexer uses the DenterHelper library for dynamic indentation handling.

Features:
	
 	--Dynamic handling of INDENT and DEDENT tokens.
 	--Support for Python-like syntax, including:
	--Assignments, expressions, and control statements (if, elif, else, while, for).
	--Comparison operators (<, <=, >, >=, ==, !=).
	--Logical operators (and, or, not).
	--Support for arrays, variables, strings, and numbers.
	--Parse tree visualization using Graphviz.
	--Commandline parse tree visualization.


  
Requirements

	Environment
  		Operating System: Cross-platform (tested on Windows 10, MacOS 13)
  		Python Version: Python 3.8 or later
  		ANTLR Version: ANTLR 4.13.2

	Python Libs
		antlr4-python3-runtime==4.13.2
		graphviz (only if you want an image of the parse tree.)


To install the required libraries, run:

	pip install antlr4-python3-runtime graphviz
 
Setup Instructions

1. Clone the Repository

Clone this repository to your local machine:

	 git clone https://github.com/printfastt/Pythonparser

3. Install ANTLR

Download and set up ANTLR:

Download ANTLR4 jar file.

Place the jar file in a preferred directory (e.g., /usr/local/lib).

Add an alias for ANTLR to your shell configuration file:

 alias antlr4='java -jar /usr/local/lib/antlr-4.13.2-complete.jar'


5. Generate Lexer and Parser Files
Run the following commands to generate the lexer and parser files:

		 antlr4 -Dlanguage=Python3 python.g4


6. Run the Parser
Ensure the main.py, pythonLexer.py, pythonParser.py, and Denter.py files are in the same directory. Then run:

		 python main.py


Key Files:

		python.g4: ANTLR grammar file defining the Python-like syntax.
		
		Denter.py: Local copy of the DenterHelper library for dynamic indentation handling (https://github.com/yshavit/antlr-denter/tree/main)
		
		main.py: Driver script to parse Python-like scripts and visualize the parse tree.

    		pythonLexer.py and pythonParser.py: Auto-generated files by ANTLR.



Example Usage
Place the Python-like script to be parsed in the file project_deliverable_3.py.
Run the parser:

		 python main.py
The script outputs the token stream, the parse tree in textual format, and a graphical representation (parse_tree.png).

Notes:

The dynamic indentation support is powered by DenterHelper. This library has been locally downloaded to avoid dependency issues. (See Denter.py for details.)
