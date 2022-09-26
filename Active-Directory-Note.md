# Set up
- Install Windows Server 2019
- Install Winsdows 10
## Setup Server Network Adapters
![Setup image](C:\Users\ainaf\OneDrive\Desktop\Git\Notes\Setup Server Network Adapters.png)
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
- Server Manager - add roles and features
- Next -- Server Roles [*] Remote Access
- Install Routing (Role services)
- Tools-Routing and Remote Access-DC(local)
## Install and Configure DHCP
- Server Manager - add roles and features
- Next -- Server Roles [*] DHCP
- Tools-DHCP(setup scope)
  - IPv4-Newscope
- Ipv4-Server Options-Config- [*]003 Router
  -IP address 172.16.0.1-Add-Apply
- Right click dc.domain...-All Tasks-Restart
## Enable Browsing on the DC
- Sever Manager-Configure this local server
- Turn off IE Enhanced Security Configuration
## PowerShell Scripts from GitHub
- Download the powershell script to Desktop
- Open Windows PowerShell ISE
- Change to the directory 
- Click play
## Install Window 10 & join to Domain
- Settings-About-Rename this PC(advanced)
- click Change
- Rename Computer name "CLIENT1"
- Rename Member of "mydomain.com"
- Type username & Password of admin or users allowed
- Restart


