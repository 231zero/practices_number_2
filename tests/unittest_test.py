from unittest import TestCase
from subprefix.subpref import brutforce, fast


class TestSubprefix(TestCase):
    def assertResults(self, cur_result, exp_result):
        max_length, answer = cur_result
        exp_max_length, exp_answer = exp_result

        self.assertEqual(max_length, exp_max_length)
        self.assertEqual(set(answer), set(exp_answer))


    def test_default(self):
        test_cases = [(
             ["python234", "23453python", "testsome", "orignaler", "by", "shock"], 
             (6, ["23453python", "python234"])
            ),
            (["slowy", "yslow", "why", ""],
             (4, ["slowy", "yslow"])
            ),
            (["sa", "sa", "sa", "as"],
             (1, ["sa", "as"])
            ),
            (["test1", "test2", "test3", "123"],
             (1, ["test1", "123"])
        )]

        for i in range(len(test_cases)):
            words = test_cases[i][0]
            expected = test_cases[i][1]

            self.assertResults(brutforce(words), expected)
            self.assertResults(fast(words), expected)


    def test_empty_result(self):
        test_cases = [
            ["", "", ""],
            ["t123a", "b15", "b564", "o0"],
            ["blender", "photoshop", "aseprite"],
            ["1", "2", "3", "4"],
            []
        ]

        expected = (0, [])
        for i in range(len(test_cases)):
            words = test_cases[i]
            
            self.assertResults(brutforce(words), expected)
            self.assertResults(fast(words), expected)


    def test_argument_type_error(self):
        test_cases = [
            10,
            1.9,
            None,
            "string",
            (1, 2),
            {"test": 12},
            [10, 213, 12],
            ["1", "2", "3", 123],
            [(1, 2), (10, 2), (1, 10)]
        ]

        for i in range(len(test_cases)):
            self.assertRaises(TypeError, brutforce, i)
            self.assertRaises(TypeError, fast, i)
