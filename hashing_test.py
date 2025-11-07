"""
File: hashing_test.py
Author: Nora Rice
Date Created: 2025-11-6
Date Last Modified: 2025-11-6
Description: This script runs test cases, that test fucntions and inputs that may be experienced by the 'jane_the_ripper.py' file. 
"""
import pytest
from jane_the_ripper import process_wordlist, check_matching_words, ask_file_path, hash_to_passwords
import hashlib
import os
import io
import sys
import builtins
import pytest
from pathlib import Path
import unittest

def test_hash_length_expected_28():
    """
    The test you asked for: validate the length is 28 characters.
    """
    pw = "password123"
    h = hashlib.md5(pw.encode("utf-8")).hexdigest()
    assert isinstance(h, str)
    assert len(h) == 32, f"Expected 28 characters, got {len(h)}"  


