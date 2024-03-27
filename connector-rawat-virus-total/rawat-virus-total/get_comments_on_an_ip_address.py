import urllib

from .make_rest_api_call import MakeRestApiCall


def get_comments_on_an_ip_address(config: dict, params: dict) -> dict:
    endpoint = "/api/v3/ip_addresses/"+params.get('ipaddress')+"/comments"  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    queryp ={'limit' : int(params.get('limit'))}
    params = queryp

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response