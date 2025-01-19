"""
pytest 테스트 코드
"""

from print import hello_world


def test_hello_world():
    """
    hello_world 함수를 테스트하는 함수
    """
    assert hello_world() == "Hello World!"
