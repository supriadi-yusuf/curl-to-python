import requests
import os
import json

def api_request(offset):

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-CA,en;q=0.9,id;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'ocp-apim-subscription-key': '291a9190a1c6453fb7ae13c799ae5665',
        'origin': 'https://www.petsathome.com',
        'pet-care-platform-search-uid': 'uid=3521047367546:v=16.0:ts=1726455305084:hc=1',
        'priority': 'u=1, i',
        'referer': 'https://www.petsathome.com/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-pcp-correlation-id': '0f26a032-1e2b-4e3e-9ff2-2bf9b9b815f0',
        'x-pcp-correlation-session-id': '2cb73b0f-12d1-482a-b3d4-afb12e8f0213',
        'x-pcp-origin': 'web/pcp',
        'x-pcp-principal-correlation-id': '22524776-68d2-4756-97d2-d073b7ef9489',
        'x-pcp-referrer': '/search',
    }

    params = {
        'searchTerm': 'dog',
        'offset': offset,
        'limit': '100',
        'sortBy': 'best-match',
        'searchType': 'Product',
    }

    response = requests.get('https://api2.petsathome.com/cs/ecomm/api/v1/search', params=params, headers=headers)

    for product in response.json()["products"]:
        yield product

if __name__ == '__main__':

    products = []
    for offset in range(0, 5000, 100):
        for product in api_request(offset):
            print(product["itemId"])
            products.append(product)

    try:
        os.mkdir("results")
    except FileExistsError:
        pass

    with open("results/products.json", "w") as json_file:
        json.dump(products, json_file)