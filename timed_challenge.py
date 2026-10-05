# Timed Challenge: Remove Duplicates (Keep Order)
# Return the values in the order they first appeared, without duplicates.
# Input: ["apple", "banana", "apple", "kiwi", "banana"]
# Output: ["apple", "banana", "kiwi"]

def remove_duplicates(values):
    """
    Return values in their original order without duplicates.
    """
    if not isinstance(values, list):
        return []

    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


# Tests
if __name__ == "__main__":
    print(remove_duplicates(["apple", "banana", "apple", "kiwi", "banana"]))
    # Expected: ["apple", "banana", "kiwi"]

    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
    # Expected: [1, 2, 3, 4]

    print(remove_duplicates([]))
    # Expected: []

    print(remove_duplicates(["A", "A", "A"]))
    # Expected: ["A"]

    print(remove_duplicates("apple"))
    # Expected: []

# Reflection (200-300 words)
#
# For this challenge, I chose a set along with a list. I used the set to keep
# track of values that I had already seen, because checking if a value is in a
# set is usually O(1). I used a list for the final answer because I needed to
# keep the values in the same order that they first appeared. This combination
# made the problem simple while still being efficient.
#
# The 30-minute time limit affected my decision because I wanted to choose a
# solution that I already understood instead of trying to build something more
# complicated. I first thought about what the problem needed to do, then picked
# a set because duplicates needed to be found quickly. After that, I used a
# list to store the values that were not already seen. Working under a time
# limit made me focus on getting a correct solution first instead of trying to
# make the code overly complicated.
#
# One trade-off I made was using extra memory for the set. The set takes
# additional space, but it makes checking for duplicates much faster than
# searching through the result list every time. I also added a check for an
# incorrect input type so the function returns an empty list instead of
# causing an error. Overall, I chose a simple solution that I could explain,
# test, and finish within the time limit. This challenge showed me that in a
# technical interview, it is important to choose a data structure that solves
# the problem efficiently while also making sure the solution is realistic to
# complete under pressure.
