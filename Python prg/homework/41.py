tasks = []
tasks.append("task 1")
tasks.append("task 2")
tasks.append("task 3")

print(f"After adding task 1, task 2, task 3 {tasks}")

tasks_backup = tasks.copy()
print(f"Back of the task list {tasks_backup}")

tasks.extend(["task 4", "task 5", "task 6"])
print(f"After adding task {tasks}")

tasks.insert(0,"urgent task")
print(f"Afetr adding 'urgent task' at  the begging.{tasks}")

tasks.remove("task 3")
print("After removing 'task3:,tasks")
print("\n")

graders=(85,90,78)
print=(graders[01])
            