from solutions.CHK.checkout_solution import checkout


class TestChk():
    def test_not_existing_item(self):
        assert checkout('ABSD') == -1

    def test_single_pieces(self):
        assert checkout('ABCD') == 115

    def test_special_offer(self):
        assert checkout('AAAA') == 180
