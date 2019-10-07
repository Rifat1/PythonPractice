
MAX_PID=5000
MIN_PID=300
pid=[0]*(MAX_PID-MIN_PID)
def allocate_map():
    
    if pid==None:
        return -1
    for i in range (len(pid)):
        pid[i]=None
    return 1
def allocate_pid():
    if pid==None:
        return -1
    for i in range(len(pid)):
        if pid[i]==None:
            pid[i]=1
            allocatedPid=i+MIN_PID
            print (allocatedPid)
            return allocatedPid
            # break
    return -1
    # print(i+MIN_PID)
    # return i+MIN_PID
            
def release_pid(newPid):
    newPid=newPid-MIN_PID
    pid[newPid]=None
    


allocate_map()
allocate_pid()
allocate_pid()
release_pid(300)
allocate_pid()
allocate_pid()

