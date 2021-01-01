from decimal import Decimal
from unittest import mock
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Category, Notebook, CartProduct, Cart, Customer
from .utils import recalc_cart
from .views import AddToCartView, BaseView

User = get_user_model()


class ShopTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Ноутбуки', slug='notebooks')
        image = SimpleUploadedFile('notebook_image.jpg', content=b'', content_type='image/jpeg')
        self.notebook = Notebook.objects.create(
            category=self.category,
            title='Test Notebook',
            slug='test-slug',
            image=image,
            price=Decimal('50000.00'),
            diagonal='17.3',
            display_type='ips',
            processor_freq='3.4 GHz',
            ram='6 GB',
            video='GeForce GTX',
            time_without_charge='10 hours'
        )
        self.customer = Customer.objects.create(user=self.user, phone='11111111221', address='Address')
        self.cart = Cart.objects.create(owner=self.customer)
        self.cart_product = CartProduct.objects.create(
            user=self.customer,
            cart=self.cart,
            content_object=self.notebook

        )

    def test_add_to_cart(self):
        self.cart.products.add(self.cart_product)
        recalc_cart(self.cart)
        self.assertIn(self.cart_product, self.cart.products.all())
        self.assertEqual(self.cart.products.count(), 1)
        self.assertEqual(self.cart.final_price, Decimal('50000.00'))

    def test_response_from_add_to_cart_view(self):
        factory = RequestFactory()
        request = factory.get('')
        request.user = self.user
        response = AddToCartView.as_view()(request, ct_model='notebook', slug='test-slug')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart/')

    def test_mock_homepage(self):
        mock_data = mock.Mock(status_code=444)
        with mock.patch('mainapp.views.BaseView.get', return_value=mock_data) as mock_data_:
            factory = RequestFactory()
            request = factory.get('')
            request.user = self.user
            response = BaseView.as_view()(request)
            self.assertEqual(response.status_code, 444)
