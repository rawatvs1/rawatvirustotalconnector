from rawat-virus-total.check_health import _check_health
from .data import config


def test_check_health():
    resp = _check_health(config)
    assert resp == True