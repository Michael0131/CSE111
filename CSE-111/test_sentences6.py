from prove_assignment6 import *
import pytest

def test_get_determined():
    for i in range(69):
        singular_determiners = ['the','a','many','some']
        word = get_determiner(determiner_var)
        assert word in singular_determiners

pytest.main(["-v","--tb=line","prove_assignment6.py"])
