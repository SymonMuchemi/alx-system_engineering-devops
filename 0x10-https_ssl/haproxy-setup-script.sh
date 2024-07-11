#!/usr/bin/env bash
# sets up HAProxy to handle encrypted traffic using
# a cerificate from Certbot

# update package
apt update

# install HAProxy
apt install haproxy

# install Certbot
apt install certbot

# obtain the certificate
certbot --standlone -d www.symonmuchemi.tech

# cetificate will
#  be stored in `/etc/letsencrypt/live/www.symonmuchemi.tech`

# create a combined file containing both the certificate
# and the private key
cat /etc/letsencrypt/live/www.symonmuchemi.tech/fullchain.pem /etc/letsencrypt/live/www.symonmuchemi.tech/privkey.pem > /etc/haproxy/certs/www.symonmuchemi.tech.pem

# ensure permission are set correctly
chmod 600 /etc/haproxy/certs/www.symonmuchemi.tech.pem

# add the following configuration sot the haproxy
echo "
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log     global
    mode    http
    option  httplog
    option  dontlognull
    timeout connect 5000
    timeout client  50000
    timeout server  50000
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http

frontend front_conf
        bind *:443 ssl crt /etc/haproxy/certs/www.symonmuchemi.tech.pem
        mode http
        option forwardfor
        http-request set-header X-Forwarded-Proto https if { ssl_fc }
        default_backend webservers

backend webservers
        mode http
        balance roundrobin
        server web-01 54.157.149.106:80 check
        server web-02 18.210.14.198:80 check

" > /etc/haproxy/haproxy.cfg

# create an index.html file in the web server's root directory
echo "Holberton School" | sudo tee /var/www/html/index.html

# restart the nginx
sudo systemctl restart nginx

# restart haproxy to apply new configurations
sudo systemctl restart haproxy
