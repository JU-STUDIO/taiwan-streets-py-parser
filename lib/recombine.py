import json

def recombine_json(json_path:str, uri:list):

    _list = list()
    _street_name_list = list()

    with open(json_path) as file:

        street = json.load(file)
  
        for item in street:
            _street_name_list.append(item['street_name'])

    _list = {
        "city" : uri['city'],
        "area" : uri['area'],
        "street_name" : _street_name_list
    }

    json_writer(_list)

def json_writer(stree_list:list):

    json_path = 'report/tw_streets.json'

    with open(json_path, 'a+') as file:
        json.dump(stree_list, file, indent=4, ensure_ascii=False)