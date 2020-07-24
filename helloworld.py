import asana

# replace with your personal access token. 
personal_access_token = '1/712677614983068:cea1a3725eb49ac9d21fd473066261e9'

# Construct an Asana client
client = asana.Client.access_token(personal_access_token)
# Set things up to send the name of this script to us to show that you succeeded! This is optional.
client.options['client_name'] = "hello_world_python"

# Get your user info
me = client.users.me()

# Print out your information
print("Hello world! " + "My name is " + me['name'] + "!")