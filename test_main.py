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
def test_mix_names_everyone_get_present(names):
    pairs = main.mix_names(names)
    has_present = []; make_present = []
    for pair_index in range(len(pairs)):
        make_present.append(pairs[pair_index][0])
        has_present.append(pairs[pair_index][1])

    has_present_verification = []; make_present_verification = []

    for name in names:
        has_present_verification.append(name in make_present)
        make_present_verification.append(name in has_present)

    everyone_has_present = False not in has_present_verification
    everyone_make_present = False not in make_present_verification
    is_everything_perfect= False not in [everyone_has_present, everyone_make_present]
    assert is_everything_perfect