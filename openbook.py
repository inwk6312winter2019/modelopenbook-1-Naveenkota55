file=open("running-config.cfg","r")
term = "nameif"
term2="ip address"
dict={}
def list_ifname_ip():
        for line in file:
                line.strip().split('/n')
                if term in line:
                        line_nameif=line.replace('nameif','')
                        print (line_nameif)
                if term2 in line:
                        line_ip_address=line.replace('ip address','')
                        print (line_ip_address)
                
                #dict.update({line_nameif:line_ip_address})
                

list_ifname_ip()
print (dict)
file.close()





