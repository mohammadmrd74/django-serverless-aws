from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from .dynamoDB import DynamoDBManager
dynamodb = DynamoDBManager(table_name='pyws')
class DataBase_test(TestCase):
    #check if database is working
    def create_data(self):
        
        dbResponse = dynamodb.put_item({
                    'id': {'S': '/devices/id6'},
                    'deviceModel': {'S': '/devicemodels/id1'},
                    'name': {'S': 'sensor'},
                    'note': {'S': 'a note'},
                    'serial': {'S': 'A020000102'}
                  }
                 )
        
        self.assertEqual(dbResponse["ResponseMetadata"]["HTTPStatusCode"], 200)

class GetDeviceTests(TestCase):
    def test_create_device(self):
        # Data to be used in the POST request
        data = {
            "id": "/devices/id3",
            "deviceModel": "/devicemodels/id3",
            "name": "New Device",
            "note": "Testing new device.",
            "serial": "C030000104"
        }
        
        response = self.client.post(reverse('device-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_missing_information(self):
        data = {
            "id": "/devices/id1",
            "note": "Testing a sensor.",
            "serial": "A020000102"
        }
        
        response = self.client.post(reverse('device-create'), data, format='json')
        response_data = response.json()
        #check if it has a name and model property because it should contain a validation error
    
        self.assertIn("deviceModel", response_data)
        self.assertIn("name", response_data)


class AddDeviceTests(TestCase):
    def test_get_device_by_id(self):
        device = dynamodb.get_item({
                        'id': {'S': "/devices/id1"}
                })

        # if finding was successful
        response = self.client.get(reverse('device-get', args=[device.id.split("/")[-1]]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], device.id)
        self.assertEqual(response.data['deviceModel'], device.deviceModel)

    def test_get_device_not_found(self):
        # if there wasn't any device
        response = self.client.get(reverse('device-get', args=["id3"]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_get_device_exception_error(self):
        # i write a case in the code to test a simulated exception
        response = self.client.get(reverse('device-get', args=["exception"]))

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
