#!/usr/bin/env bash
# Prepare web servers for deployment
apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" >/data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data

new_str="server {\nlocation /hbnb_static {\nalias /data/webstatic/current;\n}\n}"
sed -i "/http {/ a $new_str" /etc/nginx/nginx.conf

service nginx restart
