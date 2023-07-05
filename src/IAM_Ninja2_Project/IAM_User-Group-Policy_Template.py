import os
from jinja2 import Template

# Get the user information - DynamoDB, System Manager Parameter Store

user_names = ['StudentOne', 'StudentTwo', 'StudentThree', 'StudentFour', 'StudentFive']

# Define the CloudFormation template using Jinja syntax
template = Template("""
AWSTemplateFormatVersion: '2010-09-09'
Description:
  Create IAM Users.

Resources:
  RandomStringCustomResource:
    Type: "Custom::RandomString"
    Properties:
      length: 25
      ServiceToken: !ImportValue RandomizerLambdaArnB2301 # Importing value exported by another cloudformation template

  StudentsReadOnlyGroup:
    Type: AWS::IAM::Group
    Properties:
      GroupName: StudentsReadOnlyGroup
#      Policies:
#        - Policy

  StudentsReadOnlyPolicy:
    Type: AWS::IAM::Policy
    Properties:
      Groups:
        - !Ref StudentsReadOnlyGroup
      PolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Action: '*'
            Resource: '*'
      PolicyName: StudentsReadOnlyPolicy

{% for user_name in user_names %}
  Student{{user_name}}:
    Type: AWS::IAM::User
    Properties:
      Groups:
        - !Ref StudentsReadOnlyGroup
      LoginProfile:
        Password: !GetAtt RandomStringCustomResource.RandomString
        PasswordResetRequired: true
      UserName: Student{{user_name}}
{% endfor %}     

Outputs:
 RandomString:
    Description: RandomString Value
    Value: !GetAtt RandomStringCustomResource.RandomString
""")

# Render the template with the provided data
rendered_template = template.render(user_names=user_names)

# Get the content root path
content_root = os.path.dirname(os.path.abspath(__file__))

# Print the content root path
print(f"The content root path is: {content_root}")

template_path = content_root + '/generated-template/template.yaml'
# Save the rendered template in a file
with open(template_path, 'w') as file:
    file.write(rendered_template)