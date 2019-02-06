file=open("running-config.cfg","r")
file1=open("new_config.cfg","a")
def update_ip():
        for line in file:
               
                line=line.strip().replace('192','10')
                line=line.strip().replace('172','10')
                line=line.strip().replace('255.255.0.0','255.0.0.0')
                line=line.strip().replace('255.255.255.0','255.0.0.0')
                print (line)
                file1.write(line)
update_ip()


file.close()



'''
                
        if term in line:
                        line_nameif=line.replace('nameif','')
                        line_nameif=line_nameif.strip()
                        print (line_nameif)
                if term2 in line:
                        line_ip_address=line.replace('ip address','')
                        line_ip_address=line_ip_address.strip()
                        line_ip_address=line_ip_address.replace(' ',',')
                        print (line_ip_address)
                        dict.update({line_nameif:line_ip_address})
                        
                ("255.255.0.0"/"255.255.255.0") to "255.0.0.0"
'''
