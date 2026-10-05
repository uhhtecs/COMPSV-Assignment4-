"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
"""

def has_duplicates(product_ids):
    # A set is a good choice because it only stores unique values and lets us
    # check whether a value was already seen in about O(1) average time.
    # We go through the list once, so the overall expected runtime is O(n).
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support
removing tasks from the front.
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        # A deque works well because tasks are added to the back and removed
        # from the front. Both operations are O(1) on average.
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None
        return self.tasks.popleft()


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to
return the number of unique values seen so far.
"""

class UniqueTracker:
    def __init__(self):
        # A set stores each value only once, so adding and checking values
        # takes O(1) average time. Getting the number of unique values is O(1).
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# Simple tests
if __name__ == "__main__":
    print(has_duplicates([10, 20, 30, 20, 40]))  # True
    print(has_duplicates([1, 2, 3, 4, 5]))        # False

    task_queue = TaskQueue()
    task_queue.add_task("Email follow-up")
    task_queue.add_task("Code review")
    print(task_queue.remove_oldest_task())         # Email follow-up
    print(task_queue.remove_oldest_task())         # Code review
    print(task_queue.remove_oldest_task())         # None

    tracker = UniqueTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    print(tracker.get_unique_count())               # 2
