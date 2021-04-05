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
        {   #? Change the values to any integer values from 1 to 5 (as all feature values are binned into 5 bins)
            'smokers_pc': "0",
            'adults_obese_pc': "0",
            'food_env_index': "0",
            'physically_inactive': "0",
            'access_exercise_pc': "0",
            'excess_drinking_pc': "0",
            'uninsured_pc': "0",
            'vaccinated_pc': "0",
            'highschool_rate': "0",
            'some_college_pc': "0",
            'unemployed_pc': "0",
            'children_poverty_pc': "0",
            'income_ratio': "0",
            'single_parent_pc': "0",
            'crime_rate': "0",
            'avg_daily_pm2.5': "0",
            'severe_housing_prob': "0",
            #? Once all your preferred values have been set, run the python file and the results will be shown in the terminal
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