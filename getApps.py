import urllib2

import time

import globalVar as GlobalVar
import tool as getRandString
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

    if(appUp == True):
        injectString = raw_input("Enter random parameter to inject: ")
        print "Using " + injectString + " for injection testing.\n"

    if "?" not in appURL:
        print "No URI parameters provided for GET request...Check your options.\n"
        raw_input("Press enter to continue...")
        return ()
    split_uri = appURL.split("?")
    if split_uri[1] == '':
        raw_input(
            "No parameters in uri.  Check options settings.  Press enter to return to main menu...")
        return ()
#    randomUri = buildUri(appURL, injectString)  891

#def buildURL(origURL,randValue)
