Zabbix template check ssl
==========================

Tested on Zabbix Version 3.2

FEATURES
--------
* CommonName
* Remaning days 90,30 and 15
* Validity Certificate  
* Serial
* Version



REQUIREMENTS
------------
* Zabbix server version 3.2
* Python 3.x

INSTALLATION
------------
* Agent
  * Copy __userparameter_ssl.conf__ to __/etc/zabbix/zabbix_agentd.d/userparameter_ssl.conf__
  * Copy cert.py to /opt/bin/cert.py
  * Restart zabbix_agent
* Server
  * Import template __template_ssl.xml__ file


LICENSE
-------
GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
