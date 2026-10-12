
import os
import pm4py
from datetime import datetime , date , timedelta
import random
import pandas as pd
import numpy as np
                 
################################################################################## ایجاد و شبیه سازی ایونت لاگ

EventLog = pd.DataFrame(columns=['Case-Id', 'Activity', 'Time-Stamp'])
hw4 = pd.read_csv("C:/Users/98912/Desktop/Process mining/HW4.csv" , header=None)

id = 1
i=0
for i in range(22):
    for j in range(int(hw4.iloc[i, 0])):
        for k in range(1, 18):
            if pd.notna(hw4.iloc[i,k]):
                df = pd.DataFrame({
                    "Case-Id": [id],
                    "Activity": [hw4.iloc[i, k]],
                    "Time-Stamp": datetime.now() + timedelta(days=id)
                })
                EventLog = pd.concat([EventLog, df], ignore_index=True)
        id += 1


EventLog = pm4py.format_dataframe(EventLog, case_id='Case-Id', activity_key='Activity', timestamp_key='Time-Stamp')
event_log = pm4py.convert_to_event_log(EventLog)




############################################################################################## تعداد کل کیس ها
total_case = id-1



################################################################################################## رسم گراف DFG اولیه
dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
pm4py.view_dfg(dfg, start_activities, end_activities)





############################################################################################## رسم ماتریس dependency

print('\n\n\n محاسبه dependency matrix:')

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dependency_matrix = pd.DataFrame(index=index, columns=columns)

Activities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for j in Activities:
    for k in  Activities:
        dependency = dfg[(j,k)]
        dependency_matrix.at[j,k] = dependency

print(dependency_matrix)





############################################################################################################# رسم گراف  DFG با شاخص تواتر 4 و شاخص میزان وابستگی 95%

print('\n\n\n محاسبه Correlation matrix و حذف یال های زیر 0.95 در dfg:')
dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
dfg95 = dfg

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Correlation_matrix = pd.DataFrame(index=index, columns=columns)

Activities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for j in Activities:
    for k in  Activities:
        Correlation = (abs(dfg95[(j,k)])-abs(dfg95[(k,j)]))/(abs(dfg95[(j,k)]) + abs(dfg95[(k,j)]) + 1)
        if abs(Correlation) < 0.95:
            del dfg95[(j,k)]
        Correlation_matrix.at[j, k] = round(Correlation , 3)

print(Correlation_matrix)
pm4py.view_dfg(dfg95, start_activities, end_activities)



dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
dfg4 = dfg
Activities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for j in Activities:
    for k in  Activities:
        if dfg4[(j,k)] <= 4:
            del dfg4[(j,k)]
            dependency = 0
        dependency = dfg4[(j,k)]
        dependency_matrix.at[j, k] = dependency
print('\nچاپ ماتریس بر اساس شاخص تواتر L>4:\n\n')
print(dependency_matrix)
pm4py.view_dfg(dfg4, start_activities, end_activities)

dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)







############################################################################################################# ج.1 - تعداد دفعاتی که h در فرایند امده
print('\n\n\n جواب سوال 1:')
act_pos_h = pm4py.get_activity_position_summary(event_log, 'h', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
h_number=0
for key in act_pos_h.keys():
    print('Number of "h" in position',key,'=' ,act_pos_h[key])
    h_number += act_pos_h[key]
print('Total number of "h" in event log =', h_number)




######################################################################################################## ج.2 - تعداد دفعاتی که c , d بلافاصله بعد از هم امده اند
print('\n\n\n جواب سوال 2:')
filtered_log_c_d = pm4py.filter_directly_follows_relation(event_log, [('c','d'),('d','c')], activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
variants_c_d = pm4py.get_variants(filtered_log_c_d, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
c_d_number=0
for key in variants_c_d.keys():
    c_d_number += len(variants_c_d[key])
print('Total number of directly follow of "c,d" in event log =', c_d_number)




###################################################################################################################### ج.3 - مقدار دوباره کاری ها
print('\n\n\n جواب سوال 3:')
total_rework = pm4py.get_rework_cases_per_activity(event_log, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
print('Naumber of total rework:')
print(total_rework)
print('Activities "d,e" are the most repeated. but just "d" has self rework.')


self_rework = pm4py.filter_directly_follows_relation(event_log, [('d','d')], activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
variants_rework_d = pm4py.get_variants(self_rework, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

d_rework=0
for key in variants_rework_d.keys():
    d_rework += len(variants_rework_d[key])
print('Naumber of self rework "d":', d_rework)
print(variants_rework_d.keys())

act_pos_d = pm4py.get_activity_position_summary(event_log, 'd', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
d_number=0
for key in act_pos_d.keys():
    d_number += act_pos_d[key]
    
activities_freq = dict(EventLog["concept:name"].value_counts())


print('rate of rework "d": (rework(d)/Freq.(d))*100  = %' , (d_rework/activities_freq['d'])*100)





###################################################################################################### ج.4 - happy path
print('\n\n\n جواب سوال 4:')
filtered_log_top1_variant = pm4py.filter_variants_top_k(event_log, 1, activity_key='concept:name', timestamp_key='time:timestamp', case_id_key='case:concept:name')
top1variant = pm4py.get_variants(filtered_log_top1_variant, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
print('the happy path of process: \n ',list(sorted(top1variant.keys())))




###################################################################################################### ج.5 - واریانت هایی که از مسیر اصلی عبور نمی کنند
print('\n\n\n جواب سوال 5:')
filtered_log_not_happy_path = pm4py.filter_variants(event_log, [('a', 'c', 'd', 'e', 'h')], False , activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
not_on_happy_path_variant = pm4py.get_variants(filtered_log_not_happy_path, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
print((len(filtered_log_not_happy_path)/total_case)*100, '% of the variants do not cross the happy path: \n\n',list(sorted(not_on_happy_path_variant.keys())))





###################################################################################################### ج.6 - سه واریانت اصلی
print('\n\n\n جواب سوال 6:')
filtered_log_top3_variant = pm4py.filter_variants_top_k(event_log, 3, activity_key='concept:name', timestamp_key='time:timestamp', case_id_key='case:concept:name')
top3variant = pm4py.get_variants(filtered_log_top3_variant, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
x=list(sorted(top3variant.keys()))
total_top3variant = 0
print('Three main variants of the process:')
for key in top3variant.keys():
    print(key,'=',len(top3variant[key]))
    total_top3variant +=len(top3variant[key])

print('The 3 main variants are %',(total_top3variant/total_case)*100,'of all cases.\n\n\n\n')





###################################################################################################################محاسبه شاخص تعین نوع getway
print('\n\n\n محاسبه شاخص تعین نوع getway:')

getway_a_cd = (abs(dfg[('c','d')])+abs(dfg[('d','c')]))/(abs(dfg[('a','c')]) + abs(dfg[('a','d')]) + 1)
print('Getway=',getway_a_cd)




#################################################################################################################محاسبه شاخص long distance b,f
print('\n\n\n محاسبه شاخص long distance:')

long_bf= (2*(10)/(activities_freq['b'])+(activities_freq['f'])+1)-(2*abs((activities_freq['b'])-(activities_freq['f']))/((activities_freq['b'])+(activities_freq['f'])+1))
print('Lond distace b&f=',long_bf)















