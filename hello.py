def create_task(name,duration):
    Task = {
        "name" : name,
        "duration" : duration
    }

    return Task

def time_block(start_time,end_time):
    Time = {
        "start" : start_time,
        "end" : end_time,
        "duration_mins": 0  
    }

    t_start=Time["start"].split(":")
    t_end = Time["end"].split(":")

    block = (int(t_end[0])*60+int(t_end[1]))-(int(t_start[0])*60+int(t_start[1]) )
    Time["duration_mins"] = block

    return Time


def schedule(tasks,time_block):
    min_used = time_block["duration_mins"]
    task_list = []
    for task in tasks:
        if task["duration"]<=min_used:
            min_used = min_used - task["duration"]
            task_list.append(task)
    return task_list


task1 = create_task("Study Physics", 60)
task2 = create_task("Edit YouTube Video", 30)
task3 = create_task("Work on Game Dev", 45)
task4 = create_task("Read a Book", 60)

tasks = [task1, task2, task3, task4]
block = time_block("09:00", "12:00")

result = schedule(tasks, block)

for task in result:
    print(f"Task: {task['name']} | Duration: {task['duration']} mins")


