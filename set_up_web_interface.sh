sudo apt-get update
sudo apt-get -y install apache2
sudo chmod 777 /var/www/html
sudo chmod 777 /usr/lib/cgi-bin
sudo ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled
sudo mv ./udp_web_server.cgi /usr/lib/cgi-bin/udp_web_server.cgi
sudo mv ./web_server.cgi /usr/lib/cgi-bin/web_server.cgi
sudo mv ./web_interface.html /var/www/html/web_interface.html
sudo mv ./udp_web_interface.html /var/www/html/udp_web_interface.html
sudo systemctl restart apache2
sudo chmod 777 /usr/lib/cgi-bin/udp_web_server.cgi
sudo chmod 777 /usr/lib/cgi-bin/web_server.cgi
sudo chmod 777 /var/www/html/web_interface.html
sudo chmod 777 /var/www/html/udp_web_interface.html

