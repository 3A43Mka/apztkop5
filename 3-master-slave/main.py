from master import Master


def init():
    master = Master()
    master.process([{'name': 'Wrap a present for John', 'steps': 3},
                    {'name': 'Wrap a present for Bill', 'steps': 4}])
    print("Logs:")
    print(master.get_logs())
    print("Results:")
    print(master.get_results())


if __name__ == '__main__':
    init()
