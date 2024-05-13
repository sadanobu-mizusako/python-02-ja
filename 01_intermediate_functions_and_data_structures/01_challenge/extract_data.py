import re

def extract_data(text):
    pattern = r'[a-zA-Z0-9_]+\:[a-zA-Z0-9_]+'
    matches = re.findall(pattern, text)
    return matches

def better_extract_data(text):
    pattern = re.compile(r'([a-zA-Z0-9_]+)\:([a-zA-Z0-9_]+)')
    matches = extract_data(text)

    res = []
    for m in matches:
        res_ = pattern.search(m)
        res.append((res_.group(1), res_.group(2)))

    return res

if __name__ == "__main__":
    text = "The subject has Age:25 and Height:180cm.Other details are not relevant.Weight:70kg was noted."
    matches = extract_data(text)
    print(matches) 

    res = better_extract_data(text)
    print(res) 