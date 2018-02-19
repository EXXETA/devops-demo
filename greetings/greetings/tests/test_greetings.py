from greetings.service import greeting


def test_greeting():
    assert 'Bob' in greeting('Bob')
