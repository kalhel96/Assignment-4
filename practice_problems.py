"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""



# ---------------------------------------------------------------
# Problem 1: Duplicate Tracker
# A set removes duplicates. If the set is shorter than the list,
# something was repeated.
# ---------------------------------------------------------------
def has_duplicates(product_ids):
    return len(set(product_ids)) != len(product_ids)


# ---------------------------------------------------------------
# Problem 2: Order Manager
# A queue is first in, first out, like a line at a store.
# New tasks join the back; the oldest task leaves from the front.
# ---------------------------------------------------------------
class TaskQueue:
    def __init__(self):
        self.tasks = []              # an empty line

    def add_task(self, task):
        self.tasks.append(task)      # new task goes to the BACK

    def remove_oldest_task(self):
        if len(self.tasks) == 0:     # nobody in line?
            return None
        return self.tasks.pop(0)     # take from the FRONT


# ---------------------------------------------------------------
# Problem 3: Unique Value Counter
# A set ignores repeats, so its size is the unique count.
# ---------------------------------------------------------------
class UniqueTracker:
    def __init__(self):
        self.values = set()          # an empty "no-repeats" box

    def add(self, value):
        self.values.add(value)       # repeats get ignored

    def get_unique_count(self):
        return len(self.values)      # count what's in the box


# ---------------------------------------------------------------
# Tests
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Problem 1
    print(has_duplicates([10, 20, 30, 20, 40]))  # True
    print(has_duplicates([1, 2, 3, 4, 5]))       # False
    print(has_duplicates([]))                    # False (empty)
    print(has_duplicates([7, 7, 7]))             # True  (all same)

    # Problem 2
    task_queue = TaskQueue()
    task_queue.add_task("Email follow-up")
    task_queue.add_task("Code review")
    print(task_queue.remove_oldest_task())       # Email follow-up
    print(task_queue.remove_oldest_task())       # Code review
    print(task_queue.remove_oldest_task())       # None (empty)

    # Problem 3
    tracker = UniqueTracker()
    print(tracker.get_unique_count())            # 0 (empty)
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    print(tracker.get_unique_count())            # 2
    tracker.add(-5)
    tracker.add(0)
    print(tracker.get_unique_count())            # 4