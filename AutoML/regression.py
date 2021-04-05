import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

data = {
    "data":
    [
        {
            '% Smokers': "0",
            '% Adults with Obesity': "0",
            'Food Environment Index': "0",
            '% Physically Inactive': "0",
            '% With Access to Exercise Opportunities': "0",
            '% Excessive Drinking': "0",
            '% Uninsured': "0",
            '% Vaccinated': "0",
            'High School Graduation Rate': "0",
            '% Some College': "0",
            '% Unemployed': "0",
            '% Children in Poverty': "0",
            'Income Ratio': "0",
            '% Single-Parent Households': "0",
            'Violent Crime Rate': "0",
            'Average Daily PM2.5': "0",
            '% Severe Housing Problems': "0",
        },
    ],
}

body = str.encode(json.dumps(data))

url = 'http://ad5c7ba6-2287-4c85-b766-703fb10e089f.southeastasia.azurecontainer.io/score'
api_key = '' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))