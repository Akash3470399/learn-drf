from django.test import TestCase
from .. models import Store

class StoreModelTest(TestCase):
    ''' test for Store model '''

    def setUp(self):
        Store.objects.create(
            user_id = 5, store_name="sports store", address1='main road', 
            address2='Ansing', city='Washim', zipcode='444607', country='india', 
            state='mh', phone_number='23435676', email='anu@gmail.com'
        )
        
        Store.objects.create(
            user_id = 6, store_name="puppy store", address1='main road2', 
            address2='Ansing', city='Washim', zipcode='444607', country='india', 
            state='mh', phone_number='23435676', email='anushka@gmail.com'
        )
        
    def test_store(self):
            sports_store = Store.objects.get(store_name='sports store')
            puppy_store = Store.objects.get(store_name='puppy store')

            self.assertEqual(
                sports_store.store_name, 'sports store'
            )
            self.assertEqual(
                puppy_store.store_name, 'puppy store'
            )