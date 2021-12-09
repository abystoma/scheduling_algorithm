from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Process Id", "Burst Time", "Completion Time", "Turn-Around Time","Waiting time"]
class priority:
    waiting_time=0
    turnaround_time=0
    completion_time=0
    def __init__(self,name,burst,priority):
        self.name=name
        self.burst=burst
        self.priority=priority
        
res=[]

total_waiting_time,total_turn_around_time=0,0
number_of_processes=int(input("Enter total process: "))

for i in range(1,number_of_processes+1):
    burst,importance=input('Enter burst time and priority of process: ').split()
    res.append(priority(i,int(burst),int(importance)))

res.sort(key=lambda x:x.priority)
           
# calculation of table values 
for i in range(number_of_processes):
    if i==0:
        res[i].waiting_time=0
        res[i].completion_time=res[i].burst
        res[i].turnaround_time=res[i].completion_time
    else:
        res[i].completion_time=res[i-1].completion_time+res[i].burst
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