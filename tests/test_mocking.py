from unittest.mock import MagicMock
import pytest

def test_magick_mock():
    mock = MagicMock()
    mock.__str__.return_value = 'foobarbaz'
    assert str(mock) == 'foobarbaz'