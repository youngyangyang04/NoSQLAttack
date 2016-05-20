import os

import shodan
import sys

import signal


mainMe = 1
def main():
    print "asdf"
#    signal.signal(signal.SIGINT, signal_handler)
    global optionSet
    #Set a list so we can track whether options are set or not to avoid resetting them in subsequent cals to the options menu.
    optionSet = [False]*9
    global yes_tag
    global no_tag
    yes_tag = ['y', 'Y']
    no_tag = ['n', 'N']
    global victim
    global webPort
    global uri
    global httpMethod
    global platform
    global https
    global myIP
    global myPort
    global verb
    global scanNeedCreds
    global dbPort
    #Use MongoDB as the default, since it's the least secure ( :-p at you 10Gen )
    platform = "MongoDB"
    dbPort = 27017
    myIP = "Not Set"
    myPort = "Not Set"
    mainMenu()

def mainMenu():
    global platform
    global victim
    global dbPort
    global myIP
    global myPort
    mmSelect = True
    while mmSelect:
        os.system('clear')
        print "===================================================="
        print " _   _       _____  _____ _     "
        print "| \ | |     /  ___||  _  | |   "
        print "|  \| | ___ \ `--. | | | | |   "
        print "| . ` |/ _ \ `--. \| | | | |     "
        print "| |\  | (_) /\__/ /\ \/' / |____"
        print "\_| \_/\___/\____/  \_/\_\_____/"
        print "===================================================="
        print "NoSQLAttack"
        print "sunxiuyang04@gmail.com"
        print "\n"
        print "1-Set options"
        print "2-NoSQL DB Access Attacks"
        print "3-NoSQL Web App attacks"
#        print "4-Scan for Anonymous " + platform + " Access"
#        print "5-Change Platform (Current: " + platform + ")"
        print "x-Exit"

        select = raw_input("Select an option:")
        if select == "1":
            option();
        elif select == "2":
            if(optionSet[0] == True):
                if platform == "MongoDB":
                    test = 1


def option():
    global victim
    global webPort
    global uri
    global https
    https = 1
    global platform
    global httpMethod
    global postData
    global myIP
    global myPort
    global verb
    global mmSelect
    global dbPort
    global requestHeaders
    requestHeaders = {}
    optSelect = True

    if optionSet[0] == False: #
        victim = "Not Set"
    if optionSet[1] == False:
        webPort = 80
        optionSet[1] == True
    if optionSet[2] == False: #Set App Path (Current: Not Set)
        global uri
        uri = "Not Set"
    if optionSet[3] == False:
        global httpMethod
        httpMethod = "GET"
    if optionSet[4] == False:
        global myIP
        myIP = "Not Set"
    if optionSet[5] == False:
        global myPort
        myPort = "Not Set"

    while optSelect:
        print "\n\n"
        print "Options"
        print "1-Set target host/IP (Current: " + str(victim) + ")"
        print "2-Set web app port (Current: " + str(webPort) + ")"
        print "3-Set App Path (Current: " + str(uri) + ")"
#        print "4-Toggle HTTPS (Current: " + str(https) + ")"
        print "4-Set " + platform + " Port (Current : " + str(dbPort) + ")"
        print "5-Set HTTP Request Method (GET/POST) (Current: " + httpMethod + ")"
        print "6-Set my local " + platform + "/Shell IP (Current: " + str(myIP) + ")"
        print "7-Set shell listener port (Current: " + str(myPort) + ")"
        print "x-Back to main menu"
        select = raw_input("Set an option:")

        if select == '1':
            optionSet[0] = False
            while optionSet[0] == False:
                notDNS = True
                goodDigits = True
                victim = raw_input("Enter host or IP/DNS name:")
                octets = victim.split(".")
                if len(octets) != 4:
                    optionSet[0] = True
                    notDNS = False
                else:
                    for item in octets:
                        try:
                            if int(item)<0 or int(item)>255:
                                print "Bad octets in IP address."
                                goodDigits = False
                        except:
                            notDNS = False
                if goodDigits == True or notDNS == False:
                    print "\nTarget set to:" + victim + "\n"
                    optionSet[0] = True
        elif select == '6':
            optionSet[4] = False
            while optionSet[4] == False:
                goodLen = False
                goodDigits = True
                myIP = raw_input("Enter host IP for my "+ platform +"/Shells:")
                octets = myIP.split(".")
                if len(octets) != 4:
                    print "Invalid IP length."
                else:
                    goodLen = True
                    for item in octets:
                        try:
                            if int(item)<0 or int(item)>255:
                                print "Bad octets in IP address."
                                goodDigits = False
                        except:
                            goodDigits = False
                if goodDigits == True and goodLen == True:
                    print "\nShell/DB listener set to "+ myIP +"\n"
                    optionSet[4] = True












def scanMongoDBIP():
    SHODAN_API_KEY = "9kwHl4vdqoXjeKl7iXOHMvXGT3ny85Ig";
    api = shodan.Shodan(SHODAN_API_KEY);
    try:
        results = api.search('mongoDB')

        print 'Results found:%s' % results['total']
        for result in results['matches']:
            print 'IP:%s' % result['ip_str']
            #        print result['data']
            print ' '
    except shodan.APIError, e:
        print 'Error:%s' % e

if __name__ == "__main__":
    main()