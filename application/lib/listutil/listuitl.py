from collections import Counter


def get_top_occurences_from_list(items, num_of_elements=1):
    # Check if its a list
    if isinstance(items, list) == False:
        return []

    return Counter(items).most_common(num_of_elements)
