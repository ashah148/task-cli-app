import sys

if sys.argv[1] == "add":
    with open("tasks.txt", "a") as f:
        f.write(" ".join(sys.argv[2:]) + "\n")
    print("Task added.")
elif sys.argv[1] == "list":
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task.strip()}")
elif sys.argv[1] == "clear":
    open("tasks.txt", "w").close()
    print("All tasks cleared.")
