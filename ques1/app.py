from flask import Flask, request
from fetchProducts import fetchProducts

app = Flask(__name__)

url = 'http://20.244.56.144/'

@app.route('/categories/<category_name>/products', methods=['GET'])
def getProducts(category_name):
    # getting all the parametes from the args of get requests
    n = request.args.get('n')
    company = request.args.get('company')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    page = request.args.get('page')
    sort = request.args.get('sort')
    order = request.args.get('order')

    return fetchProducts(category_name, company, min_price, max_price, n, page, sort, order)

@app.route('/categories/<category_name>/products/<product_id>')
def getProductsOnProductId(category_name, product_id):
    pass



if __name__ == '__main__':
    app.run(debug=True)