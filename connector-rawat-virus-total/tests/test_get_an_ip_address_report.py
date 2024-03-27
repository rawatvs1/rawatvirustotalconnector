"""
Unit test
"""
from rawat-virus-total.get_an_ip_address_report import get_an_ip_address_report
from .data import config
# you can move this params in data.py
params_get_an_ip_address_report = {}

def test_get_an_ip_address_report():
    resp = get_an_ip_address_report(config, params_get_an_ip_address_report)
    # write your condition here
    assert True == True