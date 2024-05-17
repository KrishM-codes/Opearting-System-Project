
class Process_Algo:
    def __init__(self,name,arrival,burst,rem_time,completion_time,start_time):
        self.name=name
        self.arrival=arrival
        self.burst=burst
        self.rem_time=burst
        self.completion_time=completion_time
        self.start_time=start_time

def srtn(processes):
    n=len(processes) #processes-list of all proceses, n-total no. of processes
    completed_process=0 #no. of comp. processes
    total_time=0
    current_time=0
    queue=[] #ready queue
    gantt_chart=[]

    while(completed_process<n):
        for p in processes :
            #put all processes in the list(queue) who have their arrival time less than the ongoing time
            if p.arrival <= current_time and p.rem_time>0:
                queue.append(p)
        
        if(not queue):
            gantt_chart.append([current_time,'--',current_time+1])
            current_time+=1
            continue
        
        #sort the queue based on whose remaining time is least
        queue.sort(key=lambda p: p.rem_time)
        
        #remove any duplicate process from the queue
        #the queue appends the processes over the processes from the previous iteration
        #this may lead to addition of a process that is already present in the queue from the previous iteration
        
        index = 1 #index --> keeps track of duplicate elements index 
        for i in range(1, len(queue)):
            if queue[i] != queue[i - 1]:
                queue[index] = queue[i]
                index += 1
        del queue[index:]
        
        #choosing the process which has the least remaining time
        current_proc=queue[0]
        queue.pop(0)
        
        # ab process execute hoga
        if(current_proc.rem_time==current_proc.burst):
            current_proc.start_time=current_time
        
        gantt_chart.append([current_time,current_proc.name,current_time+1])
        current_proc.rem_time -= 1
        total_time+=1
        current_time+=1
        
        #if process ends
        if(current_proc.rem_time==0):
            current_proc.completion_time=current_time
            completed_process += 1
            # print("1 process comp")


    # print("all complete")
    
    output=[]

    for p in processes :
        turn_around=p.completion_time-p.arrival
        waiting_time=turn_around-p.burst
        response_time= p.start_time-p.arrival
        li=[p.name,p.arrival,p.burst,p.completion_time,turn_around,waiting_time,response_time]
        output.append(li)
        # print("TAT:" + str(turn_around) + "   WT:" + str(waiting_time) + "   RT:" + str(response_time)+"\nGantt Chart"+str(gantt_chart))
    
    i=1
    while(i<len(gantt_chart)):
        if(gantt_chart[i][1]==gantt_chart[i-1][1]):
            gantt_chart[i][0]=gantt_chart[i-1][0]
            gantt_chart.pop(i-1)
        else:
            i+=1
    
    output.append(gantt_chart)
    # print(gantt_chart)
    return output

##main kaam
# if __name__ == "__main__":
#     processes = [
#         Process_Algo(1, 0, 4,0,0,0),
#         Process_Algo(2, 1, 5,0,0,0),
#         Process_Algo(3, 5, 7,0,0,0),
#     ]
#     srtn(processes)