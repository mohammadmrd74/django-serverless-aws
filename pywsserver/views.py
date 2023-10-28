from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DeviceSerializer
from .dynamoDB import DynamoDBManager


dynamodb = DynamoDBManager(table_name='pyws')
class DeviceCreateView(APIView):
    def post(self, request):
        
        try:
            serializer = DeviceSerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                response = dynamodb.put_item({
                    'id': {'S': validated_data['id']},
                    'deviceModel': {'S': validated_data['deviceModel']},
                    'name': {'S': validated_data['name']},
                    'note': {'S': validated_data['note']},
                    'serial': {'S': validated_data['serial']}
                  }
                 )
                
                return Response(response["data"], status=response["status"])
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(2, e)
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class DeviceGetOne(APIView):
    def get(self, request, id):
        try:
            # this is just for test purposes and I want to just simulate an exception
            if id == "exception":
                raise Exception("Simulated Exception")
            else:
                
                device = dynamodb.get_item({
                        'id': {'S': "/devices/" + id}
                })
                
        except Exception as e:
            print(e)
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # serializer = DeviceSerializer(device)
        return Response(device["data"], status=device["status"])