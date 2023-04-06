import json
import requests

from tqdm import tqdm
from time import sleep

from urllib.parse import quote
from lib.recombine import recombine_json

def make_uri(city_area:list):
    
    uri_list = list()

    for city_list in city_area:
        
        city_name = city_list['name']
        area_list = city_list['area']

        for i in range(len(area_list)):  

            city = city_name
            area = area_list[i]['name']

            city_encode = quote(city)
            area_encode = quote(area)

            uri = f'https://www.post.gov.tw/post/internet/Postal/streetNameData_zip6.jsp?city={city_encode}&cityarea={area_encode}'
            
            _uri = {
                'uri' : uri,
                'city' : city,
                'area' : area,
            }

            uri_list.append(_uri)

    return uri_list

def addr_parser(uri_list:list, sleep_secs:float):
    
    for uri in tqdm(uri_list):
    
        print(uri['city'], uri['area'])
        sleep(sleep_secs)
        
        saved_path = f"./data/{uri['city']}-{uri['area']}.json"

        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"} 
        response = requests.get(uri['uri'], headers = headers)

        with open(saved_path, 'w') as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)

        recombine_json(saved_path, uri)