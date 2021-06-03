import random, numpy
import math

e = 2


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


class System:
    def __init__(self, task_generator, operators):
        self.time = 0
        self.task_generator = task_generator
        self.operators = operators

    def process(self):
        self.time += 0.1 ** e
        self.task_generator.process(self)
        for operator in self.operators:
            operator.process(self)


def time_format(time):
    days = int(time // (24 * 60))
    time = time % (24 * 60)
    hours = int(time // 60)
    time = time % 60
    time, minutes = math.modf(time)
    minutes = int(minutes)
    seconds = int(time * 60)
    return f"{days} дней {hours} часов {minutes} минут {seconds} секунд"


class Computer:
    def __init__(self):
        self.timer = 0
        self.state = "WAIT"
        self.await_time = 0
        self.execute_time = 0
        self.task = None

    def take_task(self, task):
        self.state = "EXECUTE"
        self.timer = 10
        self.task = task

    def process(self):
        if self.timer > 0:
            if self.state == "EXECUTE" or self.state == "CORRECT_EXECUTE":
                self.execute_time += 0.1 ** e
                self.task.execute_time += 0.1 ** e
            elif self.state == "ERROR":
                self.await_time += 0.1 ** e
            self.timer -= 0.1 ** e

        else:
            self.timer = 0
            if self.state == "EXECUTE":
                if random.random() < 0.7:
                    self.state = "ERROR"
                    self.timer = 3
                else:
                    self.state = "WAIT"
            elif self.state == "ERROR":
                self.state = "CORRECT_EXECUTE"
                self.timer = 10
            elif self.state == "CORRECT_EXECUTE":
                self.state = "WAIT"
            else:
                self.await_time += 0.1 ** e


class Operator:
    def __init__(self, computers):
        self.timer = 0
        self.computers = computers
        self.tasks = []
        self.task = None
        self.await_time = 0
        self.execute_time = 0
        self.correct_time = 0

    def take_task(self, task):
        self.process_time = 12
        self.task = task

    def process(self, system):
        for computer in self.computers:
            if computer.state == "WAIT":
                if computer.task:
                    system.task_generator.completed.append(computer.task)
                    computer.task = None
                if self.tasks:
                    computer.take_task(self.tasks.pop(0))

            if computer.state != "ERROR" and computer.state != "WAIT":
                computer.process()

        for computer in self.computers:
            if computer.state == "ERROR":
                computer.process()
                self.correct_time += 0.1 ** e
                return

        if self.timer > 0:
            self.timer -= 0.1 ** e
            self.execute_time += 0.1 ** e
        else:
            self.timer = 0
            if self.task:
                self.tasks.append(self.task)
                self.task = None
            if system.task_generator.tasks:
                self.task = system.task_generator.tasks.pop(0)
                self.timer = 12
            else:
                self.await_time += 0.1 ** e


print("Введите параметры задачи")
print("Kоличество задач")
if str := input():
    task_number = int(str)
else:
    task_number = 0

print("Максимальное время работы системы (в сутках)")
if str := input():
    total_time = float(str)
else:
    total_time = 0

task_generator = TaskGenerator(0.5)
operator = Operator([Computer(), Computer()])
system = System(task_generator, [operator])

print("-----------------------------------------------------------------------------------------")
while (len(task_generator.completed) < task_number or task_number == 0) and (
        system.time < total_time * 24 * 60 or total_time == 0):
    system.process()

if task_number != 0 and (remainder := task_number - len(task_generator.completed)):
    print("Система не справилась с заданием")
    print("Количество невыполненных заданий -", remainder, f"({round((remainder / task_number) * 100, 2)})%")
else:
    print("Система успешно справилась с заданием")
print("-----------------------------------------------------------------------------------------")

print("Общее время работы системы -", time_format(system.time))
print("Общее время регистрации задач -", time_format(operator.execute_time))
print("Общее время корректировки задач -", time_format(operator.correct_time))
print("Общее время ожидания оператора -", time_format(operator.await_time))

average_task_execute = sum([task.execute_time for task in task_generator.completed])
average_task_await = sum([task.await_time for task in task_generator.completed])
print("Среднее время выполнения задачи -", time_format(average_task_execute / len(task_generator.completed)))
print("Среднее время ожидания задачи -", time_format(average_task_await / len(task_generator.completed)))

average_computer_execute = sum([computer.execute_time for computer in operator.computers]) / len(operator.computers)
average_computer_await = sum([computer.await_time for computer in operator.computers]) / len(operator.computers)
print("Среднее время работы компьютера -", time_format(average_computer_execute))
print("Среднее время простоя компьютера -", time_format(average_computer_await))

for i, computer in enumerate(operator.computers):
    print("Компьютер", i)
    print("Среднее время работы компьютера -", time_format(computer.execute_time))
    print("Среднее время простоя компьютера -", time_format(computer.await_time))
