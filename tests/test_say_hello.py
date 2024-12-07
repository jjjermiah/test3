import pytest
from just_another_python_package.main import hello


def test_say_hello():
    assert hello() == (
        "Hello from just_another_python_package, [bold magenta]World[/bold magenta]!", ":vampire:"
    )


if __name__ == "__main__":
    pytest.main()
