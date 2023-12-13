# -----------------------------------------------------------
# send a whois request to a domain
#
# (C) 2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: BSD 2-Clause License
# SPDX-License-Identifier: BSD 2-Clause License
# -----------------------------------------------------------

import whois

# set the domain name
domainName = "linux-magazine.com"
reply = whois.query(domainName)

# extract the expiration date, registrar, and name servers
expirationDate = reply.expiration_date
print("Name: %s" % reply.name)
print("Expiration date: %i.%i.%i" % (expirationDate.day, expirationDate.month, expirationDate.year))

print ("Registrar: %s" % reply.registrar)

for entry in reply.name_servers:
    print("Nameserver: %s" % entry)
