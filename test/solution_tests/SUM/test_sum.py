from solutions.SUM.sum_solution import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3
