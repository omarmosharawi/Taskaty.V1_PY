from argparse import ArgumentParser
# import argparse
from taskController import taskController as tc


def main():
    controller = tc('MyTasks.txt')

    parser = ArgumentParser(description='Simple CLI Task Manger By Omar Mohamed Sharawi')

    subparsers = parser.add_subparsers()

    # parser = argparse.ArgumentParser(description='List tasks')
    # parser.add_argument('--all', action='store_true', help='List all tasks')

    # parser_list = subparsers.add_parser('list', help='List tasks')
    # parser_list.add_argument('all', nargs='?', default=False, help='List all tasks')

    add_task = subparsers.add_parser('add', help='Add a new task to the list', )
    add_task.add_argument('title', help='The title of the task', type=str)
    add_task.add_argument('-d', '--description', help='Short description of the task', type=str, default=None)
    add_task.add_argument('-s', '--start_date', help='Date to begin the task', type=str, default=None)
    add_task.add_argument('-e', '--end_date', help='Date of end the task', type=str, default=None)
    add_task.add_argument('--done', help='Check whether the task is done or not', default=False)
    add_task.set_defaults(func = controller.add_task)

    # list_task = subparsers.add_parser('list', help='List all tasks in the list')
    # list_task.add_argument('-unf', '--unfinished', help='List unfinished', action='store_true')
    # list_task.set_defaults(func = controller.display)
    list_tasks = subparsers.add_parser('list', help='List unfinished tasks')
    list_tasks.add_argument('-a', '--all', help='List all the tasks', action='store_true')
    list_tasks.set_defaults(func=controller.display)


    check_task = subparsers.add_parser('check', help='Check the given task')
    check_task.add_argument('-t', '--task', help='Task ID to be checked. If not specified, last task will be removed.', type=int)
    check_task.set_defaults(func = controller.check_task)

    remove_task = subparsers.add_parser('remove', help="Remove the given task")
    remove_task.add_argument('-r', '--remove', help='The task will be removed by (Number)', type=int)
    remove_task.set_defaults(func = controller.remove_task)

    reset = subparsers.add_parser('reset', help='Remove all tasks')
    reset.set_defaults(func = controller.reset)

    args = parser.parse_args()
    args.func(args)



if __name__ == '__main__':
    main()
