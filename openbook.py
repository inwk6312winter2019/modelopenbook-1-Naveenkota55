file=open("running-config.cfg","r")
term = "nameif"
term2="ip address"
def list_ifname_ip():
        for line in file:
                line.strip().split('/n')
                if term in line:
                        print (line)
                if term2 in line:
                        print (line)
               

list_ifname_ip()
file.close()







'''

	for lines in fin:
		lines1=lines.split()
		print (lines)
'''
