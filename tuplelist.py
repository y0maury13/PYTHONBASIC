def remove_duplicates(tuples_list):
    # Convert the list to a set to remove duplicates, then convert it back to a list
    return list(set(tuples_list))

# Example usage
tuples_list = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (7, 8)]
result = remove_duplicates(tuples_list)
a=int(input("Enter any Number:"))
print(result,a)