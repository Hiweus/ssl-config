#!/usr/bin/env python3
# Based on article avaliable in
# https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04

import os

# generating ssl keys
os.system("openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt")


# generating simetric key for handshake
os.system("openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048")


# writing configuration file 
os.system("cp ./ssl-params.conf /etc/apache2/conf-available/ssl-params.conf")

# backuping configuration file
os.system("cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf.bak")



os.system("cp ./default-ssl.conf /etc/apache2/sites-available/default-ssl.conf")

os.system("a2enmod ssl")
os.system("a2enmod headers")
os.system("a2ensite default-ssl")
os.system("a2enconf ssl-params")
os.system("apache2ctl configtest")

os.system("service apache2 restart")
os.system("service apache2 status")

