import pytest
import main


def test_read_names():
    names = main.read_names('test_names.txt')
    assert names == ['Name1', 'Name2', 'Name3', 'Name4']

@pytest.mark.parametrize('names', [('Name1', 'Name2', 'Name3', 'Name4')])
def test_mix_names(names):
    pairs = main.mix_names(names)
    assert isinstance(pairs, list)
    assert pairs[0][0] != pairs[0][1]