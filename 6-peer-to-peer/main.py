from peer import Peer


def main():
    peer1 = Peer(['Data from peer1'])
    peer2 = Peer(['Data from peer2'])
    peer1.connect(peer2)
    peer1.get_data()
    peer1.disconnect()
    print(peer1.data)


if __name__ == '__main__':
    main()
