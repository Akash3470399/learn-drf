import json
from django.http import response
from rest_framework import serializers, status
from django.test import TestCase, Client
from django.urls import reverse
from .. models import Store
from .. serializers import StoreSerializer


# initilizing APIClient app

client = Client()

class StoreViewTest(TestCase):
    def setUp(self):

        # data to be store in db
        self.sports_store = Store.objects.create(
            user_id = 5, store_name="sports store", address1='main road', 
            address2='Ansing', city='Washim', zipcode='444607', country='india', 
            state='mh', phone_number='23435676', email='anu@gmail.com'
        )
        
        self.puppy_store = Store.objects.create(
            user_id = 6, store_name="puppy store", address1='main road2', 
            address2='Ansing', city='Washim', zipcode='444607', country='india', 
            state='mh', phone_number='34356476', email='anushka@gmail.com'
        )
        
        self.xyz_store = Store.objects.create(
            user_id = 7, store_name="store xyz", address1='main road3', 
            address2='Ansing', city='Washim', zipcode='444607', country='india', 
            state='mh', phone_number='44335676', email='anshuman@gmail.com'
        )


        # data for post request
        self.valid_store_data = {
                "user_id": 2, "store_name": "valid store name", "address1": "valid address", "address2": "valid address2",
                "city": "city name here", "zipcode": "444420", "country": "xyz", "state": "xyz", "phone_number": "43546522",
                "email": "test@gmail.com"
            }

        self.invalid_store_data = {
                "user_id": 2, "store_name": "", "address1": "valid address", "address2": "valid address2",
                "city": "city name here", "zipcode": "444420", "country": "xyz", "state": "xyz", "phone_number": "43546522",
                "email": "noemail"
            }




    def test_get_all_stores(self):
        ''' test for get list of stores endpoint (list view)'''
        response = client.get(reverse('store-list'))   #API response

        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many = True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_store(self):
        ''' test for get specific store (detail view)
            1. test for valid store id
            2. test for invalid store id
        '''

        # for valid store id
        response = client.get(reverse('store-detail', kwargs={'pk':self.xyz_store.pk}))

        store = Store.objects.get(pk = self.xyz_store.pk)

        serializer = StoreSerializer(store)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # for invalid store id
        response = client.get(reverse('store-detail', kwargs={'pk':23}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_store(self):
        ''' test for post request to API
            with 
            1. valid data
            2.invalid data
        '''
        # for valid data
        response = client.post(
            reverse('store-list'), 
            data=json.dumps(self.valid_store_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # for invalid data
        response = client.post(
            reverse('store-list'), 
            data=json.dumps(self.invalid_store_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_store_update(self):
        ''' test update store endpoint
            for 1. valid data
                2. invalid data
        '''

        # for valid data
        valid_data = self.valid_store_data.copy()
        valid_data['store_name'] = 'updated_store_name'
        response = client.put(
            reverse('store-detail', kwargs={'pk':self.puppy_store.pk}),
            data=json.dumps(valid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # for invalid data
        invalid_data = self.invalid_store_data.copy()
        response = client.put(
            reverse('store-detail', kwargs={'pk':self.puppy_store.pk}),
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_store_delete(self):
        '''
        test for delete a store object
        for 1. valid store id
            2. invalid store id
        '''
        self.assert_(True, 'delete')
        # for valid store id
        response = client.delete(
            reverse('store-detail', kwargs={'pk':self.puppy_store.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # for invalid store id
        response = client.delete(
            reverse('store-detail', kwargs={'pk':34})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

