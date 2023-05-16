from server import Server
from broker import Broker


def main():
    h_server = Server("High Tier Server")
    m_server = Server("Medium Tier Server")
    l_server = Server("Low Tier Server")
    broker1 = Broker(h_server, m_server, l_server)

    # client calls server
    l_client_request = {'subscription': 'low'}
    broker1.process(l_client_request)

    h_client_request = {'subscription': 'high'}
    broker1.process(h_client_request)

    print(l_client_request)
    print(h_client_request)


if __name__ == '__main__':
    main()

