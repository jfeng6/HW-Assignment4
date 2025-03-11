"""
Unit tests for app.py
"""

from ..app import add_numbers

def test_add_numbers():
    """Test for the add_numbers function"""
    assert 3 == add_numbers(1,2)
