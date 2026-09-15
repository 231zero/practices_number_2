import pytest
from subprefix.subpref import brutforce, fast


@pytest.mark.parametrize("words,exp_max_length,exp_answer", [
    (["python234", "23453python", "testsome", "orignaler", "by", "shock"], 
     6, 
     ["23453python", "python234"]),
    (["slowy", "yslow", "why", ""],
     4, 
     ["slowy", "yslow"]),
    (["sa", "sa", "sa", "as"],
     1, 
     ["sa", "as"]),
    (["test1", "test2", "test3", "123"],
     1, 
     ["test1", "123"])
])
def test_same_results(words: list[str], exp_max_length: int, exp_answer: list[str]):
    brut_max_length, brut_answer = brutforce(words)
    fast_max_length, fast_answer = fast(words)

    assert brut_max_length == exp_max_length
    assert len(brut_answer) == 2
    for i in brut_answer: assert i in exp_answer

    assert fast_max_length == exp_max_length
    assert len(fast_answer) == 2
    for i in fast_answer: assert i in exp_answer


@pytest.mark.parametrize("words", [
    (["", "", ""]),
    (["t123a", "b15", "b564", "o0"]),
    (["blender", "photoshop", "aseprite"]),
    (["1", "2", "3", "4"]),
    ([])
])
def test_empty_result(words: list[str]):
    brut_max_length, brut_answer = brutforce(words)
    fast_max_length, fast_answer = fast(words)

    assert brut_max_length == 0
    assert brut_answer == []

    assert fast_max_length == 0
    assert fast_answer == []


@pytest.mark.parametrize("words", [
    (10),
    (1.9),
    (None),
    ("string"),
    ((1, 2)),
    ({"test": 12}),
    ([10, 213, 12]),
    (["1", "2", "3", 123]),
    ([(1, 2), (10, 2), (1, 10)])
])
def test_argument_type_error(words):
    with pytest.raises(TypeError):
        brutforce(words)
