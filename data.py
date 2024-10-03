from faker import Faker

fake = Faker()


class UserData:
    registered_user_data = {
        "email": "ArtemSokoLoveTest@yandex.ru",
        "password": "fuuuuuu",
        "name": "brahiozavr"
    }

    create_user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.user_name()
    }

    create_user_data_empty_required_field = {
        "email": fake.email(),
        "password": '',
        "name": fake.user_name()
    }


class OrderData:
    create_order_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa73"]
    }

    order_data_no_ingredients = {"ingredients": []}

    invalid_ingredient_hash_data = {"ingredients": ["61c0c5test", "61c0c5a71d1test"]}
