import main


def test_read_names():
    names = main.read_names('test_names.txt')
    assert names == ['Name1', 'Name2', 'Name3', 'Name4']
