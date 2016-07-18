#NoSQLAttack
#Introduction
NoSQLAttack is an open source Python tool to automate exploit MongoDB server IP around the world and disclose the database data by MongoDB default configuration weaknesses and injection attacks. 

It is base on [NoSQLMap](http://www.nosqlmap.net/index.html), tcstool's popular NoSQL injection tool and [shodan](https://www.shodan.io/), first search engine for Internet-connected devices. Some attack tests are based on and extensions of paper "Diglossia: Detecting Code Injection Attacks with Precision and Efficiency" and "No SQL, No Injection?".Presently the tool's exploits are focused MongoDB.

#Requirements
On a Debian or Red Hat based system, NoSQLAttack's dependencies will be writen in setup.py later.
And I develop this project on Pycharm COMMUNITY 2016.1 with python 2.7.10, so you can check out this project by git which integrated in Python. 

Varies based on features used:
* Shodan
* Metasploit Framework
* Python with PyMongo
* httplib2
* install MongoDB in laptop

#Building
On Debian/Ubuntu, it goes something like this:
```bash
cd NoSQLAttack
python setup.py install
```
#Usage
After building, you can run NoSQLAttack like this:
```bash
NoSQLAttack
```
Upon starting NoSQLAttack you are presented with with the main menu:
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


0-Scan attacked IP
1-Set options
2-NoSQL DB Access Attacks
3-NoSQL Web App attacks
x-Exit  
```

