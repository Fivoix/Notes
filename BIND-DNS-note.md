# Set up DNS
- Install Centos 8
- Install Centos 8 (fedora) Test DNS
## Update Centos 
- yum update (root)
    - cd /etc/yum.repos.d/
    - sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
    - sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
- dnf update (root)
## Install Bind
- 'dnf install bind bind-utils'
- Check if active 'systemctl status named'
- make sure nothings listen on port 53 'ss -tulpn'
# Configure DNS request to another Server
- 'vi named.conf'
    - make sure recursion in on(yes)
    - Create ann access control list 'acl AllowQuery {
        10.10.0.0/16;
        localhost;
        localnets;
    };'
    - Change the value of "allow-query" '{ AllowQuery; };'
    - Add forwarders under recursion (any i.e comcast 75.75.75.75;) ' forwarders {
                8.8.8.8;
    };
    forward only;
- start and enable NameD
    - 'systemctl enable named --now'
    - To check 'systemctl status named'
    - check if listen on port 53 'ss -tulpn'
- Change from localhost to localnets
    - 'vi named.conf'
        - listen-on port 53 '{ localnets; };'
    - 'systemctl restart named'
    - check 'ss -tulpn'
    - Ip address match with the vm 'ip addr sh'
# Testing
- Ds-DemoClient
    - Change IPv4 address 10.10.100.2, Netmask 255.255.0.0, Gateway 10.10.10.1
    - Change DNS address 10.10.100.1
- Ds-Demo
    - Add Dns service to firewall 'firewall-cmd --permanent --add-service=dns'
    - or 'firewall-cmd --permanent --add-port=53/tcp', 'firewall-cmd --permanent --add-port=53/udp'
    - Reload firewall 'firewall-cmd --reload'
# Create Zone File
- Ds-Demo
    - Go to named file 'cd /var/named/'
    - Create your zone file 'vi femilab.com.db'
        - $TTL 3600
          $ORIGIN femilab.com.

        @     IN SOA 	ns-demo.femilab.com. admin.femilab.com (
                        20221026		; serial number
                        3600			; refresh period
                        600			    ; retry period
                        604800			; expire time
                        1800 )			; negative ttl

        @	IN NS	ns-demofemilab.com.

            ns-demo		IN A	10.10.100.1
            kvm01		IN A	10.10.100.3
- Cheak zone 'named-checkzone femilab.com femilab.com.db'
- Change named.conf file
    - 'cd /etc/'
    - 'vi named.conf'
        - remove "forward only;"
        - Make a new zone
            - zone "femilab.com." IN {
	                    type master;
	                    file "/var/named/femilab.com.db";
	                    allow-update { none; };
               };
- Check the configurations 'named-checkconf named.conf' (notting means good)
- Restart named.cof 'systemctl restart named.conf' 'systemctl start named' 'systemctl status named' 
- Ds-DemoClient
- 'ping kvm01.femilab.com'
- 'ping ns-demo.femilab.com'
# Reference Links
- Part 1 - https://youtu.be/yoIxyMypuHk
- Part 2 - https://youtu.be/M_lBU0iyBpA