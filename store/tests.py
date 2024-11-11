from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse

# Create your tests here.

#this is used to test the views of the website in way that we can check if the views are working

class TestViews(TestCase):

        def test_store_view(self): #this is used to test the store view of the website
            response = self.client.get('/store/')
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'store/store.html')

        def test_cart_view(self):
            response = self.client.get('/store/cart/')
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'store/cart.html')

        def test_checkout_view(self):
            response = self.client.get('/store/checkout/')
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'store/checkout.html')



