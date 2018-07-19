import whois
print(whois.whois('www.baidu.com'))

'''
{
  "city": null,
  "name": null,
  "referral_url": null,
  "state": "Beijing",
  "name_servers": [
    "DNS.BAIDU.COM",
    "NS2.BAIDU.COM",
    "NS3.BAIDU.COM",
    "NS4.BAIDU.COM",
    "NS7.BAIDU.COM",
    "ns7.baidu.com",
    "ns2.baidu.com",
    "ns4.baidu.com",
    "ns3.baidu.com",
    "dns.baidu.com"
  ],
  "domain_name": [
    "BAIDU.COM",
    "baidu.com"
  ],
  "org": "Beijing Baidu Netcom Science Technology Co., Ltd.",
  "dnssec": "unsigned",
  "address": null,
  "country": "CN",
  "zipcode": null,
  "whois_server": "whois.markmonitor.com",
  "status": [
    "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited",
    "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
    "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
    "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
    "clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)",
    "clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)",
    "clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)",
    "serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)",
    "serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)",
    "serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)"
  ],
  "creation_date": [
    "1999-10-11 11:05:17",
    "1999-10-11 04:05:17"
  ],
  "expiration_date": [
    "2026-10-11 11:05:17",
    "2026-10-11 00:00:00"
  ],
  "registrar": "MarkMonitor, Inc.",
  "updated_date": [
    "2017-07-28 02:36:28",
    "2017-07-27 19:36:28"
  ],
  "emails": [
    "abusecomplaints@markmonitor.com",
    "whoisrelay@markmonitor.com"
  ]
}
'''