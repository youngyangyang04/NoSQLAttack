import urllib2

import time

import globalVar as GlobalVar
def getApps():#define the Attack method
    print "Web App Attacks (GET)"
    print "====================="
    #verify app is working
    print "checking to see if site at"+ str(GlobalVar.get_victim()) + ":" + str(GlobalVar.get_webPort()) + str(GlobalVar.get_url()) + " is up..."
    appUp = False #make flag of login successful
    if(GlobalVar.get_https() == "OFF"):
        appURL = "http://" + str(GlobalVar.get_victim()) + ":" + str(GlobalVar.get_webPort()) + str(GlobalVar.get_url())
    else:
        appURL = "https://" + str(GlobalVar.get_victim()) + ":" + str(GlobalVar.get_webPort()) + str(GlobalVar.get_url())
    requestHeaders = {}
    try:
        req = urllib2.Request(appURL, None, requestHeaders)
        appRespCode = urllib2.urlopen(req).getcode()
        if appRespCode == 200:
            normLength = int(len(urllib2.urlopen(req).read()))
            timeReq = urllib2.urlopen(req)
            start = time.time()
            page = timeReq.read()
            end = time.time()
            timeReq.close()
            timeBase = round((end - start), 3)

            if GlobalVar.get_verb() == "ON":
                print "App is up! Got response length of " + str(normLength) + " and response time of " + str(
                    timeBase) + " seconds.  Starting injection test.\n"

            else:
                print "App is up!"
            appUp = True

        else:
            print "Got " + str(appRespCode) + "from the app, check your options."
    except Exception, e:
        print e
        print "Looks like the server didn't respond.  Check your options."


