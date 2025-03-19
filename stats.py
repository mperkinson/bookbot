def get_word_count(file_text):
    words = file_text.split()
    return len(words)


def get_character_count(file_text):
    char_dict = {}
    for char in file_text:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else:
            char_dict[lower_char] += 1
    return char_dict


def sort_on(dict):
    return dict["count"]


def sort_char_dict(dict):
    dict_list = []
    for char, count in dict.items():
        temp_dict = {}
        temp_dict["char"] = char
        temp_dict["count"] = count
        dict_list.append(temp_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
