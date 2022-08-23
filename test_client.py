import pytest
from client import Client
import logging


cli = Client()
KEY_WORDS = ['complete', 'task']


def test_taskList():
    response = cli.taskList()
    logging.info("testing task list")
    logAssert(response.status_code == 200, "Task list no received")
    logAssert(len(response.text) != 2, "list task is empty")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "test_input,expected",
    [("this is task", "true"),
     ("test create task function", "false"),
     pytest.param("task", "this is not boolean", marks=pytest.mark.xfail)]
)
def test_createTask(test_input, expected):
    response = cli.createTask(test_input, expected)
    logging.info("testing create task list")
    logAssert(response.status_code == 200, "Task not created")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "test_input,expected",
    [("this is task", "true"),
     ("test create task function", "false"),
     pytest.param("task", "this is not boolean", marks=pytest.mark.xfail)]
)
def test_modifyTask(test_input, expected):
    response = cli.modifyTask(test_input, expected)
    logging.info("testing modify a task")
    logAssert(response.status_code == 200, "Unsuccess modify task")
    assert response.status_code == 200


def test_completeTask():
    response = cli.completeTask()
    logging.info("testing complete task")
    logAssert(response.status_code == 200, "Task not mark as completed")
    assert response.status_code == 200


def test_incompleteTask():
    response = cli.incompleteTask()
    logging.info("testing incomplete task")
    logAssert(response.status_code == 200, "Task not mark as incomplete")
    assert response.status_code == 200


def test_deleteTask():
    response = cli.deleteTask()
    logging.info("testing delete task")
    logAssert(response.status_code == 200, "Task not was deleted")
    assert response.status_code == 200


def logAssert(test, msg):
    if not test:
        logging.error(msg)
        assert test, msg
