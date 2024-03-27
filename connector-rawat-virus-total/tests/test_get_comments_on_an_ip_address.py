"""
Unit test
"""
from rawat-virus-total.get_comments_on_an_ip_address import get_comments_on_an_ip_address
from .data import config
# you can move this params in data.py
params_get_comments_on_an_ip_address = {}

def test_get_comments_on_an_ip_address():
    resp = get_comments_on_an_ip_address(config, params_get_comments_on_an_ip_address)
    # write your condition here
    assert True == True