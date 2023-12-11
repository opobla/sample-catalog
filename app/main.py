from flask import jsonify, request, Flask
from catalog import get_products, create_product

app = Flask(__name__)

@app.route('/product', methods=['GET', 'POST'])
def list_all_products():
    '''This view manages the CRUD of products'''
    if request.method == 'GET':
        response = get_products()
        return jsonify(response)
    
    if request.method == 'POST':
        data = request.get_json()
        data['sku'] = data['sku'] if 'sku' in data else None
        create_product(
            data['sku'],
            data['title'],
            data['long_description'],
            data['price_euro'])
        return jsonify({ "status": "ok"})


@app.route('/hello')
def hello_world():
    message = "Hola Mundo, soy Python! Ahora con CloudBuild y hablando JSON"
    response = {
        "message": message,
        "length": len(message)
    }
    return jsonify(response)

@app.route('/bye')
def bye_world():
    return ("Adios mundo cruel")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

