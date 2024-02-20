import requests

def fetch_products():
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)
    print("API Response Status Code:", response.status_code, "\n")
    return response.json()

def parse_data():

    products_data = fetch_products()
    prices = []
    ratings = []
    titles = []
    categories = set()

    for product in products_data:
        prices.append(float(product['price']))
        categories.add(str(product['category']))
        titles.append({'title': product['title'], 'id': product['id']})
        ratings.append(product['rating'])

    unique_categories = list(categories)
    unique_categories.sort()
    print("Price Stats - Max: {:.2f}, Min: {:.2f}, Average: {:.2f}\n".format(
        max(prices), min(prices), sum(prices) / len(prices)
    ))
    print("Unique Categories: {}\n".format(unique_categories))
    print("Sorted Titles:\n", sorted(titles, key=lambda p: p['title']), "\n")
    print("Sorted Ratings:\n", sorted(ratings, key=lambda p: p['rate']))

parse_data()
