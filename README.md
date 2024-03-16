# todo-list-clean-architecture
TODO cli tool applying Clean Architecture

```bash
# Project CRUD
todo-cli project -c "Project Name" -k "project-key"
todo-cli project -u project-key --name "Project Name Changed"
todo-cli -a
todo-cli project set project-key
todo-cli project rm project-key

# Todo List
todo-cli list -c "New List Created"
todo-cli list -u "List Update Name"
todo-cli list -a
todo-cli list set "List Selected"
todo-cli list rm "TODO List deleted"

# Task
todo-cli task -c "Task created" -d "Task Description"
todo-cli task -u -t "New Task Title" -d "New Task Description"
todo-cli task -a
todo-cli task complete "Task Name"
todo-cli task rm "Task Deleted"
```