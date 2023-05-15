from slave import Slave


class Master:
    def __init__(self):
        self.results = []
        self.logs = []
        self.slaves = []

    def process(self, tasks):
        for task in tasks:
            slave = Slave(task['name'], task['steps'])
            self.slaves.append(slave)
        while len(self.slaves):
            for slave in self.slaves:
                if slave.is_complete():
                    res = slave.get_result()
                    self.logs.append(res)
                    self.results.append(res)
                    self.slaves.remove(slave)
                else:
                    res = slave.do_task()
                    self.logs.append(res)

    def get_logs(self):
        return self.logs

    def get_results(self):
        return self.results
