# Set up
- Install Windows Server 2019
- Install Winsdows 10
## Setup Server Network Adapters
![image alt text](../../Nonsense/Setup%20Server%20Network%20Adapters.png)
- Assingn Ip Address to internal adapter
  - Give the Ip Address 172.16.0.1 Subnet mask 255.255.255.0 Defult gateway -
  - Prefered DNS - 127.0.0.1
## Rename the Sever name
 - Name - DC
## Install Active Directory Domain Services
- Server Manager - add roles and features
- Promote the server to a domain controller
 - Creates the domain.com
 - Add a new forest
## Create Domain Admin Account
- Open Active Directory Users and Computers
- Create an organization Unit for the Admin Account
- Make the User account created Admin
## Install and Configure RAS(Remote Access Server) /NAT
- 