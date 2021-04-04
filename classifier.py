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
            'smokers_pc': "1",
            'adults_obese_pc': "1",
            'food_env_index': "1",
            'physically_inactive': "1",
            'access_exercise_pc': "1",
            'excess_drinking_pc': "1",
            'uninsured_pc': "1",
            'vaccinated_pc': "3",
            'highschool_rate': "2",
            'some_college_pc': "1",
            'unemployed_pc': "1",
            'children_poverty_pc': "1",
            'income_ratio': "1",
            'single_parent_pc': "1",
            'crime_rate': "3",
            'avg_daily_pm2.5': "2",
            'severe_housing_prob': "1",
        },
    ],
}

body = str.encode(json.dumps(data))

url = 'http://3f3891a3-1f60-48eb-92c9-64710bf08a70.southeastasia.azurecontainer.io/score'
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