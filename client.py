from curses.ascii import isalpha
import requests
import json
import random
import logging

from task import Task

API = "http://127.0.0.1:5000/{}"
TASKS = "tasks"


class Client:
    def taskList(self):
        response = requests.get(API.format(TASKS))
        return response

    def getTask(self, taskId):
        endPoint = TASKS + "/" + taskId
        singleTask = requests.get(API.format(endPoint))
        return singleTask

    def createTask(self, name, complete):
        taskObj = Task(name, complete)
        taskData = taskObj.taskToJson()
        response = requests.post(API.format(TASKS), json=taskData)
        return response

    def modifyTask(self, name, complete):
        id = self.randomId()
        self.checkId(id)
        newTask = Task(name, complete)
        taskJson = newTask.taskToJson()
        endPoint = TASKS + "/" + id
        response = requests.put(API.format(endPoint), json=taskJson)
        return response

    def randomId(self):
        tasks = self.taskList().text
        json_object = json.loads(tasks)
        index = random.randint(0, len(json_object))
        logging.info("testing random id")

        # check the index is in the range
        if index == len(json_object):
            index = - 1
        try:
            id = json_object[index]["id"]
        except IndexError as e:
            id = None
        return id

    def completeTask(self):
        id = self.randomId()
        self.checkId(id)
        endPoint = TASKS + "/" + id + "/completed"
        response = requests.post(API.format(endPoint))
        return response

    def incompleteTask(self):
        id = self.randomId()
        self.checkId(id)
        endPoint = TASKS + "/" + id + "/incomplete"
        response = requests.post(API.format(endPoint))
        return response

    def deleteTask(self):
        id = self.randomId()
        self.checkId(id)
        endPoint = TASKS + "/" + id
        response = requests.delete(API.format(endPoint))
        return response

    def checkId(self, id):
        if id is None:
            exit("Error: The Task list is empty")
