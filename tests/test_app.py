import sys
import os

# Ensure Python can find the app module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add_numbers  # Import function from app.py

def test_add_numbers():
    """Test for the add_numbers function"""
    assert add_numbers(2, 3) == 5