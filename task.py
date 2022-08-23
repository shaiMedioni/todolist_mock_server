import json


class Task:
    def __init__(self, name, complete):
        self.name = name
        self.complete = complete

    def taskToJson(self):
        taskStruct = '{{"completed": {0}, "task": "{1}"}}'
        taskData = taskStruct.format(self.complete, self.name)
        return json.loads(taskData)
        