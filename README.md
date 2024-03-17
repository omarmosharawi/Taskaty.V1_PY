# Simple CLI Task Manager
Welcome to Taskaty.V1_PY, a simple yet powerful Command Line Interface (CLI) Task Manager created by Omar Mohamed Sharawi. This tool is designed to help you manage your tasks with ease and efficiency.

## Introduction
Taskaty.V1_PY is a lightweight, easy-to-use task manager that runs in your command line. It allows you to add, view, and complete tasks with simple commands. Whether you're a developer, a student, or anyone who needs to keep track of tasks, Taskaty.V1_PY is the perfect tool for you.

## Features
- **Simple Command Line Interface**: No complicated setups, just straightforward task management.
- **Add Tasks**: Quickly add tasks with descriptions, start date, and end date.
- **View Tasks**: See all your tasks in one place, see completed or unfinished tasks separately from the full list, and see the time period or time remaining between the start and end times.
- **Complete Tasks**: Mark tasks as done with a single command.
- **Persistence**: Your tasks are saved in the txt file, so you can pick up where you left off.

## Getting Started
Clone the repository to get started with Taskaty.V1_PY:
```
git clone https://github.com/omarmosharawi/Taskaty.V1_PY.git
```
```
cd Taskaty.V1_PY
```
```
venv\Scripts\activate
```
```
cd app
```
```
python app.py -h
```

## Usage
Here’s how you can use Taskaty.V1_PY to manage your tasks:
- Show help `python app.py -h`
- Show add help `python app.py add -h`
- Add a new task `python app.py add "Finish the project documentation"`
- Add a new task with details `python app.py add "Finish the project documentation" -d "using py" -s 2023-05-23 -e 2024-3-10`
- View tasks not finished `python app.py list`
- View all tasks `python app.py list -a`
- Complete a task `python app.py check -t 1`
- Remove a task `python app.py remove -r 1`
- Remove all tasks `python app.py reset`

# Contributing
Omar Mohamed Hussien Ali - @omarmosharawi
- Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
- You can report any issues or suggestions for this project by contact me via mail: omarmosharawi@gmail.com.

# Support
- Give a ⭐️ if you like this project!
