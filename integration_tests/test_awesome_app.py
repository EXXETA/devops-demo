def test_awesome_app(chrome):
    chrome.get('http://localhost:5000/Bob/1/1')

    greeting = chrome.find_element_by_id('greeting')
    result = chrome.find_element_by_id('result')

    assert 'Bob' in greeting.text
    assert result.text == '1 + 1 = 2.0'
