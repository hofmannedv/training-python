# -----------------------------------------------------------
# send a RDAP request to an IP address using IPWHOIS
#
# (C) 2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: BSD 2-Clause License
# SPDX-License-Identifier: BSD 2-Clause License
#
# Status: proof-of-concept
#
# -----------------------------------------------------------

import sys
from pprint import pprint

# add path to site-packages
# - requires adjustment -
sys.path.insert(0, '/home/frank/.local/pipx/venvs/ipwhois/lib/python3.11/site-packages')

# import class ipwhois from ipwhois module, only
from ipwhois import IPWhois

# define IPv6 address
ipAddress = "2a02:2e0:3fe:1001:302::"

# create IPWhois object
request = IPWhois(ipAddress)

# send RDAP request
reply = request.lookup_rdap(depth=1)

# print result nicely
pprint(reply)
