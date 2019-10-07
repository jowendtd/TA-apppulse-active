# encoding = utf-8
import sys
import json
import requests

def get_access_token(saas_domain, tenant_id, client_id, client_secret):
    endpoint = "https://" + saas_domain + "/openapi/rest/v1/" + tenant_id + "/oauth/token"
    headers = {
        'clientSecret': client_id,
        'clientId': client_secret
    }
    try:
        response = requests.post(endpoint, headers=headers).json()
        return response['access_token']
    except Exception, e:
        raise e