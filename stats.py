def get_num_words(content):
    words = content.split()
    return len(words)
def character_count(content):
    char_count = {}
    content = content.lower()
    for c in content:
        if c not in char_count.keys():
            char_count[c] = content.count(c)
    return char_count
def sorted_dict(content_dict):
    sorted_dict = dict(sorted(content_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
    