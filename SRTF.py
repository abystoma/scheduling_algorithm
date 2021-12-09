from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Process Id", "Arrival Time", "Burst Time", "Completion Time", "Waiting time","Turn-Around Time"]

def SRTF(arrival_time, number_of_processes, burst_time):
    #### initialize clock ####
    current_completion = 0

    #### initialize required variables ####
    turnaround_time = [0] * number_of_processes
    waiting_time = [0] * number_of_processes

    #### initialize remaining_time with burst_time ####
    remaining_time = [x for x in burst_time]

    #### initialize starting process as 0 ####
    current_process = 0
    completion_time = [0] * number_of_processes
    while True:
        #### check new processes appeared and assign current process ####
        for process_ID in range(number_of_processes):
            if current_completion >= arrival_time[process_ID] and remaining_time[process_ID] != 0:
                if remaining_time[current_process] > remaining_time[process_ID] or remaining_time[current_process] == 0:
                    current_process = process_ID

        #### check if arrival time of current process is reached ####
        if current_completion >= arrival_time[current_process]: 
            current_completion += 1
            remaining_time[current_process] -= 1
            if remaining_time[current_process] == 0:
                completion_time[current_process] = current_completion
                turnaround_time[current_process] = current_completion - arrival_time[current_process]
                waiting_time[current_process] = turnaround_time[current_process] - burst_time[current_process]
        else: 
            current_completion +=1

        #### end timeline if all processes are done ####
        if remaining_time == [0] * number_of_processes:
            break
    total_waiting_time = 0
    total_turn_around_time = 0
    
    for i in range(0,number_of_processes):
        total_waiting_time = total_waiting_time + waiting_time[i-1]
        total_turn_around_time = total_turn_around_time + turnaround_time[i-1]  
        table.add_row([i+1, arrival_time[i], burst_time[i], completion_time[i], waiting_time[i], turnaround_time[i]])
    #### Display processes along with all details ####
    print(table)
    print("\nAverage waiting time = %.5f " % (total_waiting_time / number_of_processes))
    print("Average turnaround time = %.5f " % (total_turn_around_time / number_of_processes))

number_of_processes = int(input("Enter total process: "))
arrival_time = [int(i) for i in input("Enter arrival time: ").split()]
burst_time = [int(i) for i in input("Enter burst time: ").split()]
SRTF(arrival_time, number_of_processes, burst_time)