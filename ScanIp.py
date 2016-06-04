import  shodan

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
