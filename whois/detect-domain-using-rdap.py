# -----------------------------------------------------------
# send a RDAP request to a domain
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

# add path to site-packages
# - requires adjustment -
sys.path.insert(0, '/home/frank/.local/pipx/venvs/rdap/lib/python3.11/site-packages')

# import class RdapClient from rdap module, only
from rdap import RdapClient

# define domain name
domainName = "linux-magazine.com"

# create RdapClient
rdapc = RdapClient()

# send RDAP request
reply = rdapc.get_domain(domainName)

# extract domain name
print("Name:", reply.data["ldhName"].lower())

# extract expiration date
events = reply.data["events"]
# print(events)
for entry in events:
    if entry["eventAction"] == "expiration":
        expirationTimestamp = entry["eventDate"]
        expirationDate = expirationTimestamp.split("T")[0]
        print("Ablaufdatum:", expirationDate)

# extract registrar
registrar = reply.data["entities"][0]["vcardArray"][1][1][3]
print ("Registrar: %s" % registrar)

# extract nameservers
nameservers = reply.data["nameservers"]
for entry in nameservers:
    name = entry["ldhName"].lower()
    print("Nameserver: %s" % name)
