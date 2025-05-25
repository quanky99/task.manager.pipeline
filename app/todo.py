class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"

class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        self.tasks = [Task(f"Task {i+1}", "Done" if i < 3 else "ToDo") for i in range(6)]

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]

if __name__ == "__main__":
    pool = TaskPool()
    pool.populate()
    print("ToDo Tasks:")
    for task in pool.get_open_tasks():
        print(task.title)
    print("\nDone Tasks:")
    for task in pool.get_done_tasks():
        print(task.title)