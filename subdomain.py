import requests

#getting input
pre = input("http or https:")
dns = input("Enter dns:")

#loading subdomain file
fd = open('subdomain-1000.txt','r')
subs = fd.read()
fd.close()

#making them as list by splitting them for every line break
subdomain = list(subs.split('\n'))
print(pre+"://"+dns)
for i in subdomain:
    url = pre+"://"+i+"."+dns
    print(url)
    #preparing the url
    try:
        r = requests.get(url)
        #try sending get request to the url
        if r.status_code!=404 and len(r.text)>0:
            print("     ************    ")
            print(i+" found at "+r.status_code)
            print("     ************    ")
    except:
        pass
        #if try not found just skip with pass
