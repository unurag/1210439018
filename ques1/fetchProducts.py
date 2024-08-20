import requests
from newToken import newToken

url = 'http://20.244.56.144/'

def fetchProducts(category, company, min_price, max_price, n, page=1, sort=None, order=None):
    fetchURL = f"{url}test/companies/{company}/categories/{category}/products?top={n}&minPrice={min_price}&maxPrice={max_price}"

    # calling token on every req
    token = newToken()

    headers = {
            "Authorization": f"{token['token_type']} {token['access_token']}",
            "Content-Type": "application/json"
        }

    try:
        response = requests.get(fetchURL, headers=headers)
        return response.json()
    except requests.exceptions.HTTPError as err:
        return {"error": "Unable to collect the data from the companies"}
    


