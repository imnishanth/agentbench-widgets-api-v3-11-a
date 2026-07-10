from widgets import stock
def test_stock():
    assert stock("gear") == 12 and stock("nope") == 0
