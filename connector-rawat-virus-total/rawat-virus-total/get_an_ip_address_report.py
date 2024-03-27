from .make_rest_api_call import MakeRestApiCall


def get_an_ip_address_report(config: dict, params: dict) -> dict:
    endpoint = "/api/v3/ip_addresses/"+params.get('ip_address')  # edit endpoint
    method = "GET"  # GET/POST/PUT/DELETE
    # write your code here, if needed.

    MK = MakeRestApiCall(config=config)
    response = MK.make_request(endpoint=endpoint, method=method, params=params)
    return response