import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

#Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='users',
#     KeySchema=[
#         {
#             'AttributeName': 'username',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'last_name',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'username',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'last_name',
#             'AttributeType': 'S'
#         },
#
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='users')
table = dynamodb.Table('users')

# Print out some data about the table.
print(table.item_count)

table.put_item(
   Item={
        'username': 'joedoe',
        'first_name': 'Joe',
        'last_name': 'Doe',
        'age': '25',
        'phone': '3235551212',
        'tests': 42,
        'account_type': 'standard_user',
    }
)

response = table.get_item(
    Key={
        'username': 'joedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)