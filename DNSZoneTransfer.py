#!/bin/python

import dns.query
import dns.resolver
import dns.zone
import socket
import sys

if len(sys.argv) != 2:
    print("Usage is: ./DNSZoneTrans.py <host>")
    sys.exit()  

host = sys.argv[1]

DNS = dns.resolver.resolve(host, 'NS') # Gathers nameservers; ns1.megacorpone.com, ns2, ns3, etc.
for ns in DNS:
    ns_data = ns.to_text()
    _, _, ns_ip = socket.gethostbyname_ex(ns_data) # Retrieves associated IPs for each ns.
    try:
        zone_trans = dns.zone.from_xfr(dns.query.xfr(ns_ip[0], host)) # Zone transfer
        subs = zone_trans.nodes.keys() # Enumerates subdomains from from zone transfer
        print(f"\nSuccessful zone transfer for {ns_ip[0]}")
        for sub in subs: # Lists subdomains
            print(f"Subdomain: {sub}")
    except:
        print(f"\nFailed zone transfer for {ns_ip[0]}")
