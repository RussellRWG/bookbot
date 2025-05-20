def count_words(text):
    split_text = text.split()
    return (len(split_text))

def count_characters(text):
    c_dict = {}
    for c in text.lower():
        if c.isalpha():
            if c in c_dict:
                c_dict[c] += 1
            else:
                c_dict[c] = 1
    return c_dict

def sort_on(dict):
    return dict["num"]

def sort_characters(c_dict):
    c_list = []
    for key, value in c_dict.items():
        c_list.append({"char": key, "num": value})

    c_list.sort(reverse=True, key=sort_on)
    output = ""
    for item in c_list:
        char = item["char"]
        num = item["num"]
        output += f"{char}: {num}\n"
    return(output)
