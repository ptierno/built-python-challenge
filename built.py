#!/usr/bin/env python3

import ipaddress
import requests
import sys

RIPE_URL = 'https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix'


def get_cidrs():
    res = requests.get(RIPE_URL).json()
    return res['data']['resources']['ipv4']


def ip_in_cidr_list(ip):
    try:
        ip = ipaddress.ip_address(ip)
    except ValueError:
        return False

    cidrs = get_cidrs()
    for cidr in cidrs:
        net = ipaddress.ip_network(cidr)
        if ip in net:
            return True
    return False


def main():
    if len(sys.argv) != 2:
        print('Please provide a single IP address.')
        sys.exit(1)

    res = ip_in_cidr_list(sys.argv[1])
    print("Pass" if res else "Fail")


if __name__ == "__main__":
    main()
