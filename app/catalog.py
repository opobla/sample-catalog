import sys
import uuid
from db.database import get_db

def get_products():
    db = get_db()

    cursor = db.cursor()
    postgreSQL_select_Query = "select sku, title, long_description, price from productos"

    cursor.execute(postgreSQL_select_Query)
    products = cursor.fetchall()

    response = []
    for product in products:
        response.append({
            "sku": product[0],
            "title": product[1],
            "long_description": product[2],
            "price": product[3],
        })
    return response

def create_product(sku, title, long_description, price_euro):
	''' Insertar todo esto en una bbdd '''
	print(f"Crear sku={sku} y title={title}", file=sys.stderr)
