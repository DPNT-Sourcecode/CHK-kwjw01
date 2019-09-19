from lib.solutions.CHK.checkout_solution import checkout


class TestChk():
    def test_not_existing_item(self):
        assert checkout('ABSD') == -1

    def test_single_pieces(self):
        assert checkout('ABCD') == 115

    def test_special_offer(self):
        assert checkout('AAAA') == 180

    def test_items_for_free(self):
        assert checkout('EEEBB') == 150

    def EEEEBB(self):
        assert checkout('EEEEBB') == 160

    def BEBEEE(self):
        assert checkout('BEBEEE') == 160

    def FFF(self):
        assert checkout('FFF') == 20

    def FFFA(self):
        assert checkout('FFFA') == 70