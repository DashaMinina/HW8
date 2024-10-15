"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        test_quantity = 500
        assert Product.check_quantity(product,test_quantity) == True
        test_quantity = 1500
        assert Product.check_quantity(product, test_quantity) == False
        test_quantity = 1000
        assert Product.check_quantity(product, test_quantity) == True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        buy_product = 700
        Product.buy(product, buy_product)
        assert product.quantity == 300

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            buy_product = 1300
            Product.buy(product, buy_product)
@pytest.fixture
def product_2():
    return Product("pen", 20, "This is a pen", 3000)
@pytest.fixture
def cart():
    return Cart()

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

def test_add_product(cart, product):
    cart.add_product(product, buy_count=4)
    assert cart.products[product] == 4
    cart.add_product(product)
    assert cart.products[product] == 5

def test_remove_product_positive(cart,product):
    cart.add_product(product, buy_count=5)
    cart.remove_product(product,remove_count=1)
    assert cart.products[product] == 4

def test_remove_product_negative_none(cart,product):
    cart.add_product(product, buy_count=5)
    cart.remove_product(product)
    assert cart.products == {}

def test_remove_product_negative(cart,product):
    cart.add_product(product, buy_count=5)
    cart.remove_product(product, remove_count=6)
    assert cart.products == {}

def test_clear(cart,product):
    cart.add_product(product, buy_count=5)
    cart.clear()
    assert cart.products == {}

def test_get_total_price(cart,product):
    cart.add_product(product, buy_count=5)
    assert cart.get_total_price() == 500

def test_get_total_price2(cart,product_2):
    cart.add_product(product_2, buy_count=5)
    assert cart.get_total_price() == 100

def test_get_total_price_negative(cart):
    assert cart.get_total_price() == 0

def test_buy_positive(cart,product):
    cart.add_product(product, buy_count=400)
    cart.buy()
    assert product.quantity == 600

def test_buy_positive_zero(cart, product):
    cart.add_product(product, buy_count=1000)
    cart.buy()
    assert product.quantity == 0

def test_buy_negative(cart, product):
    with pytest.raises(ValueError):
        cart.add_product(product, buy_count=1500)
        cart.buy()
