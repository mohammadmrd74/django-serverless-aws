import boto3

class DynamoDBManager:
    def __init__(self, table_name):
        self.dynamodb = boto3.client('dynamodb')
        self.table_name = table_name

    def put_item(self, item):
        try:
            print(self.table_name)
            self.dynamodb.put_item(
                TableName=self.table_name,
                Item=item,
                ConditionExpression="attribute_not_exists(id)"
            )
            return {"data": "created", "status": 200}
        except self.dynamodb.exceptions.ConditionalCheckFailedException:
            return {"data": "Duplicate item. Insertion aborted.", "status": 409}
        except Exception as e:
            return str(e)

    def get_item(self, key):
        try:
            response = self.dynamodb.get_item(
                TableName=self.table_name,
                Key=key
            )
            responseItems = response.get('Item')
            if (responseItems):
                return {"data": {key: value[list(value.keys())[0]] for key, value in responseItems.items()}, "status": 200}
            
            return {"data": "Device not found", "status": 404}
           
        except Exception as e:
            return None