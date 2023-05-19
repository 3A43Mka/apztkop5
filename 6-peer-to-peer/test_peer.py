from peer import Peer


def test_1():
    peer1 = Peer([])
    peer2 = Peer([])
    peer1.connect(peer2)
    assert peer1.connection == peer2


def test_2():
    peer1 = Peer([])
    peer2 = Peer([])
    peer1.connect(peer2)
    assert peer1.connection == peer2
    peer1.disconnect()
    assert peer1.connection is None


def test_3():
    peer1 = Peer(['hello from peer 1'])
    peer2 = Peer([])
    peer2.connect(peer1)
    peer2.get_data()
    peer2.disconnect()
    assert peer2.data == ['hello from peer 1']


def test_4():
    peer1 = Peer(['hello from peer 1'])
    peer2 = Peer([])
    peer2.connect(peer1)
    peer2.get_data()
    peer2.disconnect()
    assert peer2.data == ['hello from peer 1']
