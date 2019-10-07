# encoding = utf-8
import sys
import json
import requests

def get_items(helper, access_token, url, items=[]):
    header = {'Authorization':'Bearer ' + access_token}

    try:
        r = requests.get(url, headers=header)
        r.raise_for_status()
        response_json = json.loads(r.content)
        items += response_json['value']

        if '@odata.lastRetrievedSequenceId' in response_json:
            helper.log_debug("Next URL (@odata.lastRetrievedSequenceId): %s" % response_json['@odata.lastRetrievedSequenceId'])
            get_items(helper, access_token, response_json['@odata.lastRetrievedSequenceId'], items)
        
    except Exception, e:
        raise e

    return items