from chemistry import get_name, get_atomic_mass, \
        parse_formula, molar_mass, FormulaError
from pytest import approx
import pytest


def test_names():
    """Test the chemistry.get_name function."""
    first = get_name("As")
    assert first == "Arsenic"

    second = get_name("Be")
    assert second == "Beryllium"

    third = get_name("Li")
    assert third == "Lithium"

def test_atomic_masses():
    """Test the chemistry.get_atomic_mass function."""
    first = get_atomic_mass("As")
    assert first == 74.9216
    
    second = get_atomic_mass("Be")
    assert second == 9.012182

    third = get_atomic_mass("Li")
    assert third == 6.941



def test_parse():
    """Test the chemistry.parse_formula function."""
    first = parse_formula("PO4H2(CH2)12CH3")
    assert first == {"P":1, "O":4, "H":29, "C":13}

    second = parse_formula("H2O")
    assert second == {"H":2, "O":1}


def test_molar_mass():
    """Test the chemistry.molar_mass function."""
    first = molar_mass({"H":2, "O":1})
    assert first == approx(18.01528)
    second = parse_formula("C6H6")
    test2 = molar_mass(second)
    assert test2 == approx(78.11184)
    third = parse_formula("PO4H2(CH2)12CH3")
    test3 = molar_mass(third)
    assert test3 == approx(280.34072)
 

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=no", "test_chemistry.py"])
