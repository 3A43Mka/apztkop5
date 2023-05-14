class Slave:
    def __init__(self, task_text, steps):
        self.task_text = task_text
        self.steps = steps

    def do_task(self):
        if self.steps > 0:
            self.steps -= 1
            return f'Doing task "{self.task_text}", {self.steps} steps left.'
        return None

    def is_complete(self):
        if self.steps == 0:
            return True
        return False

    def get_result(self):
        if self.steps == 0:
            return f'Result for the task "{self.task_text}".'
        return None
