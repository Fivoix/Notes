# Set up DNS
- Install Centos 8
- Install Centos 8 (fedora) Test DNS
## Update Centos 
- yum update (root)
    - cd /etc/yum.repos.d/
    - sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
    - sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
- dnf update (root)
- dnf install bind bind-utils