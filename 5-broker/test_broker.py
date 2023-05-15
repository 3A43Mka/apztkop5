from broker import Broker

broker1 = Broker()


def test_1():
    l_client_request = {'subscription': 'low'}
    broker1.process(l_client_request)
    assert l_client_request == {'result': 'Result provided by Low Tier Server.', 'subscription': 'low'}


def test_2():
    m_client_request = {'subscription': 'medium'}
    broker1.process(m_client_request)
    assert m_client_request == {'result': 'Result provided by Medium Tier Server.', 'subscription': 'medium'}


def test_3():
    h_client_request = {'subscription': 'high'}
    broker1.process(h_client_request)
    assert h_client_request == {'result': 'Result provided by High Tier Server.', 'subscription': 'high'}
