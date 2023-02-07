def remove_first_four_chars(string):
    print(string)
    return string[5:]

def map_remove_first_four_chars(strings):
    return list(map(remove_first_four_chars, strings))