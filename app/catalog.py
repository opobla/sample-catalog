import sys
import uuid
from faker import Faker
def get_products():
    fake = Faker("es_ES")
    fake_response = []
    for i in range(1,400):
        fake_response.append({
            "sku": uuid.uuid4(),
            "title": fake.text(max_nb_chars=80),
            "long_description": fake.text(max_nb_chars=200),
            "price_euro": fake.numerify("####.##")
        })
    return fake_response

def create_product(sku, title, long_description, price_euro):
    ''' Insertar todo esto en una bbdd '''
    print(f"Crear sku={sku} y title={title}", file=sys.stderr)
