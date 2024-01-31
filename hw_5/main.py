from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
tasks = []


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: bool = False


@app.get('/')
async def index():
    return tasks


@app.get('/tasks/{task_id}')
async def get_task(task_id: str):
    filtered_tasks = [task for task in tasks if task.id == task_id]
    return filtered_tasks


@app.post('/tasks/')
async def create_task(task: Task):
    task_id = len(tasks) + 1
    task.id = task_id
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, new_task: Task):
    filtered_tasks = [task for task in tasks if task.id == task_id]

    if not filtered_tasks:
        return {'updated': False}

    task = filtered_tasks[0]

    task.title = new_task.title
    task.description = new_task.description
    task.status = new_task.status

    return {'updated': True, 'task': new_task}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    filtered_tasks = [task for task in tasks if task.id == task_id]

    if not filtered_tasks:
        return {'deleted': False}

    task = filtered_tasks[0]

    tasks.remove(task)
    return {'deleted': True, 'task': task}
