import numpy

e = 3

class System:
    def __init__(self, task_generator, machines):
        self.time = 0
        self.task_generator = task_generator
        self.machines = machines

    def process(self):
        self.time += 0.1 ** e
        self.task_generator.process(self)
        for machine in self.machines:
            machine.process(self)


class Task:
    def __init__(self):
        self.execute_time = 0
        self.await_time = 0


class TaskGenerator:
    # n - количество заданий в час
    def __init__(self, task_number):
        self.coef = 1 / task_number
        self.tasks = []
        self.completed = []
        self.next_task = self.__next_task()

    def __next_task(self):
        return round(numpy.random.exponential(self.coef), e)

    def process(self, system):
        for task in self.tasks:
            task.await_time += 0.1 ** e
        if system.time > self.next_task:
            self.tasks.append(Task())
            self.next_task = system.time + self.__next_task()


class Machine:
    def __init__(self):
        self.next_breakdown = self.__next_breakdown()
        self.timer = 0
        self.await_time = 0 # время ожидания
        self.execute_time = 0 # время выполнения задания
        self.repair_time = 0 # время ремонта
        self.breakdowns = 0 # поломка
        self.task = None # задача

    def __next_breakdown(self):
        return round(numpy.random.normal(20.0, 2.0), e)

    def __repair(self):
        return round(numpy.random.uniform(0.1, 0.5), e)

    def __preparation(self):
        return round(numpy.random.uniform(0.2, 0.5), e)

    def __performance(self):
        return round(numpy.random.normal(0.5, 0.1), e)

    def process(self, system):
        if self.timer > 0:
            if self.task:
                if system.time > self.next_breakdown:
                    self.breakdowns += 1
                    self.timer = self.__repair()
                    system.task_generator.tasks.insert(0, self.task)
                    self.task = None
                else:
                    self.task.execute_time += 0.1 ** e
                    self.execute_time += 0.1 ** e
            else:
                self.repair_time += 0.1 ** e
            self.timer -= 0.1 ** e
        if self.timer <= 0:  # станок закончил изготовление детали или починку
            self.timer = 0
            if self.task:
                system.task_generator.completed.append(self.task)
                self.task = None
            elif system.time > self.next_breakdown:
                self.next_breakdown = system.time + self.__next_breakdown()
            if system.task_generator.tasks:
                self.task = system.task_generator.tasks.pop(0)
                self.timer = self.__preparation() + self.__performance()
            else:  # время простоя станка
                self.await_time += 0.1 ** e


task_number = 500
task_generator = TaskGenerator(1)
machine = Machine()
system = System(task_generator, [machine])
while len(task_generator.completed) < task_number:
    system.process()

# machine_await_time = 0
# machine_execute_time = 0
task_await_time = 0
task_execute_time = 0
total_time = system.time

for task in task_generator.completed:
    task_await_time += task.await_time
    task_execute_time += task.execute_time
    # print(task.await_time)

print("Общее время работы станка", round(total_time, e), "ч")
print("Среднее время ожидания задачи", round(task_await_time / task_number, e), "ч")
print("Среднее время выполнения задачи", round(task_execute_time / task_number, e), "ч")
print("Время работы станка", round(machine.execute_time, e), "ч", round(100 * machine.execute_time / total_time, e),
      "% общего времени")
print("Время простоя станка", round(machine.await_time, e), "ч", round(100 * machine.await_time / total_time, e),
      "% общего времени")
print("Количество поломок", machine.breakdowns)
print("Время починки станка", round(machine.repair_time, e), "ч", round(100 * machine.repair_time / total_time, e),
      "% общего времени")
