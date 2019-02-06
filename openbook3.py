file=open("running-config.cfg","r")

term2="access-list transit_access_in"
term3="access-list fw-management_access_in"
term4="access-list global_access"

access_list2=[]
access_list3=[]
access_list4=[]
def access_list():
        for line in file:
                line.strip().split('/n')
                
                
                if term2 in line:
                    line=line.strip().replace('access-list transit_access_in extended permit ip object','')
                    line=line.strip().replace('access-list transit_access_in extended permit object-group','')
                    line=line.strip().replace(' object ','')
                    line=line.strip().replace(' ','')
                    access_list2.append(line)
                    
                    
                if term3 in line:
                    line=line.strip().replace('access-list fw-management_access_in extended permit ip object ','')
                    
                    line=line.strip().replace(' object ','')
                    line=line.strip().replace(' ','')
                    access_list3.append(line)
                if term4 in line:
                    line=line.strip().replace('access-list global_access extended permit ip any object ','')
                    
                    
                    line=line.strip().replace(' ','')
                    access_list4.append(line)

access_list()
print (access_list2)
print (access_list3)
print (access_list4)
file.close()



