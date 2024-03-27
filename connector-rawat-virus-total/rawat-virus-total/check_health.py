from .make_rest_api_call import MakeRestApiCall
from connectors.core.utils import update_connnector_config

def _check_health(config: dict) -> bool:
    try:
        endpoint = ""
        method = "GET"
        # print(config)
        config['demo'] = 'demovalue'
        update_connnector_config('rawat-virus-total', '1.0.0', config)
        print(config)
        MS = MakeRestApiCall(config=config)
        MS.make_request(endpoint=endpoint, method=method)
        return True
    except Exception as e:
        raise Exception(e)