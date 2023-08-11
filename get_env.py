import boto3


def get_file_s3(destination_file_name):
    s3 = boto3.client('s3')
    folder_path = 'automation_api/'
    object_key = folder_path + '.env'
    file_name = './' + destination_file_name
    bucket_name = 'somosf1-devops-files'
    s3.download_file(bucket_name, object_key, file_name)


def validate_environment(env_var):
    if env_var == 'PROD':
        environment = 'master'
    else:
        environment = env_var.lower()

    return environment


get_file_s3('.env')