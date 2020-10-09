from collections import Counter

def duplicate_count(text):
    char_dict = {}
    num = 0
    for sym in text.lower():
        if sym in char_dict:
            char_dict[sym] += 1
        else:
            char_dict[sym] = 1

    for key in char_dict:
        if char_dict[key] > 1:
            num += 1
    return num


duplicate_count("aAABcdeebF")




