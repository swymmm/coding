#. Write a function has_duplicates(lst) — returns True if the list has duplicates.
#  Hint: compare len(lst) to len(set(lst)).

def has_duplicates(lst):
    return len(lst) != len(set(lst))

# Test the function
test_list1 = [1, 2, 3, 4, 5]
test_list2 = [1, 2, 3, 4, 5, 1]

print(f"List has duplicates: {has_duplicates(test_list1)}")
print(f"List has duplicates: {has_duplicates(test_list2)}")