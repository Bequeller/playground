"""
This is a simple Python script that prints "Hello, World!" to the console.
"""

import sys
import os

# src 디렉토리를 모듈 경로에 추가
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


"""
! This is an important comment
? This is a question
// This is a normal comment
todo: This is a TODO comment
* This is a highlighted comment
normal comment
"""


def main():
    """
    print "Hello, World!"
    """
    print("Hello, World!")


if __name__ == "__main__":
    main()
