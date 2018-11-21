"""Test example.py"""
from example import main


def test_main(capsys):
    """Make sure we print hello world."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello World.\n"
