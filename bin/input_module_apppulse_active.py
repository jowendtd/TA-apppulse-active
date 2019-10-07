import os
import sys
import time
import json, requests, base64
import utils.auth as rauth
import utils.utils as utils
from datetime import datetime
     
def validate_input(helper, definition):
	pass
	
def collect_events(helper, ew):
    saas_domain = helper.get_arg("saas_domain")
    tenant_id = helper.get_arg("tenant_id")
    client_id = helper.get_arg("client_id")
    client_secret = helper.get_arg("client_secret")
    opt_index_name = helper.get_arg('index')
    opt_sourcetype_name = helper.get_arg('sourcetype')
    
    endpoint_token = "https://" + saas_domain + "/openapi/rest/v1/" + tenant_id + "/oauth/token"

    print(endpoint_token)

    headers_token = {'Content-Type': 'application/json' }

    data_token = {
        'clientSecret': client_secret,
        'clientId': client_id
    }

    print(headers_token, data_token)

    # Get Auth Token
    try:

        response_token = requests.post(endpoint_token, data=json.dumps(data_token), headers=headers_token)

        response_token_json = response_token.json()

        auth_token = response_token_json["token"]

        print(response_token_json["token"])
        print(response_token_json["expirationTime"])

    except Exception as e:
        raise e

    endpoint_configuration = "https://" + saas_domain + "/openapi/rest/v1/" + tenant_id + "/getConfiguration"

    headers_configuration = {"Authorization": 'Bearer ' + auth_token}

    print(headers_configuration)

    # Get Configuration
    try:

        response_configuration = requests.get(endpoint_configuration, headers=headers_configuration)
        response_configuration_json = response_configuration.json()

        for application in response_configuration_json["applications"]:

            data_application = json.dumps(application)

            # Save and Write the Serialized Object
            event = helper.new_event(data_application, time=datetime.now(), host="https://" + saas_domain, index=opt_index_name, source="getConfiguration", sourcetype=opt_sourcetype_name, done=True, unbroken=True)
            ew.write_event(event)

    except Exception as e:
        raise e


    lastRetrievedSequenceId = 0
    hasMoreDataToFetch = True

    # Get Data    
    try:

        while hasMoreDataToFetch != False:
          
            endpoint_getdata = "https://" + saas_domain + "/openapi/rest/v1/" + tenant_id + "/getData?lastRetrievedSequenceId=" + str(lastRetrievedSequenceId)

            response_getdata = requests.get(endpoint_getdata, headers=headers_configuration)

            response_getdata_json = response_getdata.json()

            lastRetrievedSequenceId = response_getdata_json["lastRetrievedSequenceId"]
            hasMoreDataToFetch = response_getdata_json["hasMoreDataToFetch"]

            for application in response_getdata_json["data"]:

                data_application = json.dumps(application)

                # Save and Write the Serialized Object
                event = helper.new_event(data_application, time=datetime.now(), host="https://" + saas_domain, index=opt_index_name, source="getData", sourcetype=opt_sourcetype_name, done=True, unbroken=True)
                ew.write_event(event)

    except Exception as e:
        raise e