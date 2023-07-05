 aws cloudformation create-stack --stack-name b2301-manage-iam-users --template-body file://manage-iam-users.yaml.yaml
 aws cloudformation create-stack --stack-name b2301-manage-iam-users --template-body file://manage-iam-users.yaml.yaml

 aws cloudformation create-change-set --stack-name b2301-manage-iam-users \
    --change-set-name first-change-set --change-set-type CREATE \
    --template-body file://manage-iam-users.yaml \
    --capabilities CAPABILITY_NAMED_IAM

 aws cloudformation validate-template --template-body file://manage-iam-users.yaml