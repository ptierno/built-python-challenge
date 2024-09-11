import sys
import pytest
import requests_mock

from unittest.mock import patch
from built import get_cidrs, ip_in_cidr_list, main, RIPE_URL

RIPE_DATA = {
    'data': {
        'resources': {
            'ipv4': [
                "23.154.176.0/24"
            ],
            'ipv6': [
                'some-ipv6-cidr'
            ]
        }
    }
}

def test_get_cidrs_only_gets_ipv4(requests_mock):
    requests_mock.get(RIPE_URL, json=RIPE_DATA)
    cidrs = get_cidrs()
    assert cidrs == ["23.154.176.0/24"]

def test_ip_in_cidr_list_invalid_ip(requests_mock):
    requests_mock.get(RIPE_URL, json=RIPE_DATA)
    assert ip_in_cidr_list("invalid ip") == False

def test_ip_in_cidr_list_contains_ip(requests_mock):
    requests_mock.get(RIPE_URL, json=RIPE_DATA)
    assert ip_in_cidr_list("23.154.176.1") == True

def test_ip_in_cidr_list_contains_ip(requests_mock):
    requests_mock.get(RIPE_URL, json=RIPE_DATA)
    assert ip_in_cidr_list("1.1.1.1") == False

def test_main_invalid_argument_count(requests_mock):
    requests_mock.get(RIPE_URL, json=RIPE_DATA)
    with patch.object(sys, 'argv', ['prog']):
        with pytest.raises(SystemExit) as exit:
            main()
        assert exit.type == SystemExit
        assert exit.value.code == 1

# flake8: noqa
