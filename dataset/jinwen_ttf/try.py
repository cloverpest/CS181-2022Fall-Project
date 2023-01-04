text_ai = []
with open("poetry_ai.txt", 'r') as f:
    text = f.read()
    # split with \n
    text_ai = text.split('\n')

text_le = []
with open("poetry_le.txt", 'r') as f:
    text = f.read()
    # split with \n
    text_le = text.split('\n')

text_xi = []
with open("poetry_xi.txt", 'r') as f:
    text = f.read()
    # split with \n
    text_xi = text.split('\n')

text_bei = []
with open("poetry_bei.txt", 'r') as f:
    text = f.read()
    # split with \n
    text_bei = text.split('\n')

text_bei = set(text_bei)
text_ai = set(text_ai)
text_le = set(text_le)
text_xi = set(text_xi)
# and
text = text_bei & text_ai & text_le & text_xi
# write text to file
with open("poetry.txt", 'w') as f:
    for line in text:
        f.write(line + '\n')
# create a dict map text to emotion
t2e = {}
for line in text:
    t2e[line] = -1

# create a json file with "content" and "emotion" attributes
# Path: D:\Shanghaitech\人工智能\CS181-2022Fall-Project
import json
with open("poetry.json", 'w', encoding="utf8") as f:
    json.dump(t2e, f, ensure_ascii=False, indent=0)

        