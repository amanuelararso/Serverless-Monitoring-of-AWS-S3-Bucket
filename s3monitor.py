import boto3
from botocore.exceptions import ClientError

def send_email():
    SENDER = "some@email.com" # must be verified in AWS SES Email
    RECIPIENT = "other@email.com" # must be verified in AWS SES Email

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    # The subject line for the email.
    SUBJECT = "Important Files changed!"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Dear Amanuel,\r\n Your files in S3 bucket named 'importantfiles2023' has recently changed \n\n "
    "You can check it out using the following link 'https://s3.console.aws.amazon.com/s3/buckets/importantfiles2023?region=us-east-1&tab=objects' on management console \n"
    "Disregard this email if it is you!"
    "**** Automatically generated from AWS Lambda  ****")
                
               
                
                
               
    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h3>Dear , </h3>
    <p>Your important files in S3 bucket named <i>importantfiles2023</i> has recently changed, You can check it out using the following link
        <a href='https://s3.console.aws.amazon.com/s3/buckets/importantfiles2023?region=us-east-1&tab=objects'><i>importantfiles2023</i></a> 
      <br> <br>
      Disregard this email if it is you! 
      
      <br> <br>
      
      **** Automatically generated from AWS Lambda  ****</p>
    </body>
    </html>
                """            

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
        
                        'Data': BODY_HTML
                    },
                    'Text': {
        
                        'Data': BODY_TEXT
                    },
                },
                'Subject': {

                    'Data': SUBJECT
                },
            },
            Source=SENDER
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

def lambda_handler(event, context):
    # TODO implement
    send_email()