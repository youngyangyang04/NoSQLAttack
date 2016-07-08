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
