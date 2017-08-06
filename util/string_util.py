def capitalize_all(s):
    s = s.lower()
    ret = []
    for word in s.split():
        ret.append(word.capitalize())
    return " ".join(ret)