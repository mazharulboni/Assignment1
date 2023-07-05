aws cloudformation create-change-set --stack-name Student-Group-Policy-users \
    --change-set-name first-change-set --change-set-type CREATE \
    --template-body file://template.yaml \
    --capabilities CAPABILITY_NAMED_IAM
