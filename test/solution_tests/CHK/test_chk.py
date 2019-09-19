from lib.solutions.CHK.checkout_solution import checkout

# it will be good to have fixed test prices
class TestChk():
    def test_not_existing_item(self):
        assert checkout('AB#D') == -1

    def test_single_pieces(self):
        assert checkout('ABCD') == 115

    def test_special_offer(self):
        assert checkout('AAAA') == 180

    def test_items_for_free(self):
        assert checkout('EEEBB') == 150

    def test_EEEEBB(self):
        assert checkout('EEEEBB') == 160

    def test_BEBEEE(self):
        assert checkout('BEBEEE') == 160

    def test_FFF(self):
        assert checkout('FFF') == 20

    def test_FFFA(self):
        assert checkout('FFFA') == 70

    def test_H(self):
        assert checkout('H') == 10

    def test_L(self):
        assert checkout('L') == 90

    def test_ABCDEFGHIJKLMNOPQRSTUVWXYZ(self):
        assert checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 837

    def test_ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ(self):
        assert checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ') == 1629

    def test_group_discount(self):
        assert checkout('ZZYYX') == 45 + 20 + 17