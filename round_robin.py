from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Process Id", "Burst Time", "Completion Time", "Turn-Around Time","Waiting time"]
class RoundRobin:
    waiting_time=0
    turnaround_time=0
    completion_time=0
    def __init__(self,name,burst):
        self.name=name
        self.burst=burst

res=[]
number_of_processes=int(input('Enter no of process:'))
quantum=int(input('Enter time quantum:'))
burst_list=[]
total_waiting_time = 0
total_turn_around_time = 0
for i in range(1,number_of_processes+1):
    burst=input('Enter burst time of process:')
    res.append(RoundRobin(i,int(burst)))
    burst_list.append(int(burst))
i=0
count=0
flag=set()
f=0
total_completion_time=0
while True:
    if burst_list[i]>0:
        if i==0 and f!=1:
            if burst_list[i]>=quantum:
                res[i].completion_time=quantum
                total_completion_time+=quantum
            else:
                res[i].completion_time=burst_list[i]
                total_completion_time+=burst_list[i]
            burst_list[i]-=quantum
        else:
            f=1
            if burst_list[i]>=quantum:
                burst_list[i]-=quantum
                total_completion_time+=quantum 
            else:
                total_completion_time+=burst_list[i]
                burst_list[i]-=quantum
            res[i].completion_time=total_completion_time
    if burst_list[i]<=0 and i not in flag:
        flag.add(i)
        count+=1
        if count==number_of_processes:
            break
    i+=1
    if i==number_of_processes:
        i=0

#calculating tat,twt
for i in range(number_of_processes):
    res[i].turnaround_time=res[i].completion_time
    res[i].waiting_time=res[i].turnaround_time-res[i].burst
    total_turn_around_time+=res[i].turnaround_time
    total_waiting_time+=res[i].waiting_time
#table printing
for i in range(number_of_processes):
    table.add_row([res[i].name, res[i].burst, res[i].completion_time,res[i].turnaround_time, res[i].waiting_time])


print(table)
print("\nAverage waiting time = %.2f " % (total_waiting_time / number_of_processes))
print("Average turnaround time = %.2f " % (total_turn_around_time / number_of_processes))