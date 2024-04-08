from code import powerset
from code import testen



def test_leer():
    assert powerset([]) == [[]]
def test_klein():
    assert powerset([1,2]) == [[],[1],[2],[1,2]]


def test_testen():
    assert testen([1,2,3]) == [[1],[2],[3],[1,2]]