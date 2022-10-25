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
        192.168.1.0/24;
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