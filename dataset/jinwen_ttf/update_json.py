import json
def update_json(old, new):
    old_dict = {}
    with open(old, 'r', encoding='utf-8') as fp:
        old_dict = json.load(fp)
        with open(new, 'r', encoding='utf-8') as fp2:
            new_dict = json.load(fp2)
            for key in new_dict.keys():
                    old_dict[key] += (new_dict[key] + 1)
    with open(old, 'w', encoding='utf-8') as fp3:
        json.dump(old_dict, fp3, ensure_ascii=False, indent=0)

update_json("poetry.json", "poetry_12000_13000.json")
update_json("poetry.json", "poetry_8000_8300.json")