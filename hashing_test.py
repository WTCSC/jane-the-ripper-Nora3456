"""
File: hashing_test.py
Author: Nora Rice
Date Created: 2025-11-06
Date Last Modified: 2025-11-06
Description: This script runs test cases, that test fucntions and inputs that may be experienced by the 'jane_the_ripper.py' file. 
"""
import hashlib
import os
import tempfile
import pytest

import jane_the_ripper

def test_md5_hash_length_():
    """
    Checks to make sure the MD5 hash is 32 characters long.
    """
    wordlist_path = tempfile.NamedTemporaryFile(mode="w", delete=False)
    wordlist_path.writelines(["password\n", "123456\n", "hello\n"])
    wordlist_path.close()

    jane_the_ripper.hash_to_passwords.clear()
    jane_the_ripper.process_wordlist(wordlist_path.name)

    for hash_hex in jane_the_ripper.hash_to_passwords.keys():
        assert len(hash_hex) == 32, f"MD5 hash '{hash_hex}' length is not 32 characters"

    os.unlink(wordlist_path.name)

def test_ask_file_path_(monkeypatch, capsys):
    """
    Checks that ask_file_path() loop untill the user enters a file that exists.
    """
    import tempfile, os

    # Create a real temporary file (valid path)
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(b"ok")
    tmp.close()

    # Simulate wrong path first, then correct one
    inputs = iter(["/no/such/file.txt", tmp.name])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = jane_the_ripper.ask_file_path("Enter path: ")
    output = capsys.readouterr().out

    assert result == tmp.name
    assert "File not found:" in output

    os.unlink(tmp.name)