import sys

if sys.argv[1] == "add":
    with open("tasks.txt", "a") as f:
        f.write(" ".join(sys.argv[2:]) + "\n")
    print("Task added.")
