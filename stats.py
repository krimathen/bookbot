def get_num_words(text):
    counter = 0
    word_list = text.split()
    for word in word_list:
        counter += 1
    return counter

def letter_count(text):
    character_counts = {}
    for character in text:
        char = character.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def data_sort(data):
    sorted_list = []
    
    for key, value in data.items():
        sorted_list.append({"char": key, "num": value})

    def sort_on(dict):
        return dict["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

