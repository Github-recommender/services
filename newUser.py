from github3 import login
import boto3, json, decimal
from boto3.dynamodb.conditions import Key, Attr
from creds import username, password

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)




def newUser(event, context):
    username = event["username"]

    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
    usersTable = dynamodb.Table('GRUsers')


    returnValue = username+'; '


    gr = login(username, password=password)
    user = gr.user(username)
    if user:
        response = usersTable.get_item(Key={'username':username})
        try :
            response['Item']
            returnValue=returnValue+'username exists in table; '# +'response:'+response
        except:
            usersTable.put_item(
                Item={
                    'username':username
                }
            )
            returnValue=returnValue+' username added to table; '
        return returnValue
    else:
        return "Invalid username"
