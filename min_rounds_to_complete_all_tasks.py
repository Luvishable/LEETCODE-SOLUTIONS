"""
2244. Minimum Rounds to Complete All Tasks
Medium

You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task.
In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2.
- In the second round, you complete 2 tasks of difficulty level 3.
- In the third round, you complete 3 tasks of difficulty level 4.
- In the fourth round, you complete 2 tasks of difficulty level 4.
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
"""


def minimum_rounds(tasks):
    tasks_dict = {}
    for task in tasks:
        if task not in tasks_dict:
            tasks_dict[task] = 1
        else:
            tasks_dict[task] += 1

    counter = 0
    for key, value in tasks_dict.items():
        if value % 6 == 1 and value != 1:
            counter += (((value // 5) * 2) + 1)
        elif value % 6 == 2:
            counter += ((value // 3) + 1)
        elif value % 6 == 3 or value % 6 == 0:
            counter += (value // 3)
        elif value % 6 == 4:
            counter += ((value // 5) * 2)
        elif value % 6 == 5:
            counter += ((value // 3) + 1)

    return counter


if __name__ == '__main__':
    tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
    print(minimum_rounds(tasks) )
















































