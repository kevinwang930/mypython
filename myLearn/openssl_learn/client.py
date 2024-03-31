import requests

# URL to make a request to
url = 'https://localhost:12345'

# Path to the generated certificate file
cert_file = 'cert/cert.pem'

# Make a GET request with the certificate
response = requests.get(url, cert=cert_file)

# Print the response
print(response.text)