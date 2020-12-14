import pytest
import main

names_template = ('Name1', 'Name2', 'Name3', 'Name4')


def test_read_names():
    names = main.read_names('test_names.txt')
    assert names == ['Name1', 'Name2', 'Name3', 'Name4']


@pytest.mark.parametrize('names', [names_template])
def test_mix_names(names):
    pairs = main.mix_names(names)
    assert isinstance(pairs, list)


@pytest.mark.parametrize('names', [names_template])
def test_mix_names_pairs_different(names):
    pairs = main.mix_names(names)
    is_pair_different = []
    for pair_index in range(len(pairs)):
        same_person = pairs[pair_index][0] == pairs[pair_index][1]
        is_pair_different.append(same_person)
    are_all_pairs_different = True not in is_pair_different
    assert are_all_pairs_different


@pytest.mark.parametrize('names', [names_template])
def test_mix_names_everyone_get_present():
    pass