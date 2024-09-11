# Built Python Challenge

Simple python program which;

* Takes an IP address as a command line argument
* Gets json data from the RIPE network coordination center
* Uses the `['data']['resources']['ipv4']` block in the json above to determine whether the IP
provided on the CLI is in any of the CIDRs
* *Output a Pass/Fail result based on the presence of the IP address in the CIDR ranges

## Setup

```
pip install -r requirements.txt
```

## Example

```
$ ./built.py 97.1.1.1
Pass

$ ./built.py 87.1.1.1
Fail
```

## Unit tests

Unit tests are written with `pytest`

```
$ pytest --verbosity=1
======================================= test session starts ========================================
cachedir: .pytest_cache
rootdir: /Users/ptiern/code/built
plugins: requests-mock-1.12.1
collected 4 items

test_built.py::test_get_cidrs_only_gets_ipv4 PASSED                                           [ 25%]
test_built.py::test_ip_in_cidr_list_invalid_ip PASSED                                         [ 50%]
test_built.py::test_ip_in_cidr_list_contains_ip PASSED                                        [ 75%]
test_built.py::test_main_invalid_argument_count PASSED                                        [100%]

======================================== 4 passed in 0.10s =========================================
```
