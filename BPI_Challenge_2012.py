
import os
import pm4py
from datetime import datetime , date , timedelta
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
   

dataframe = pm4py.read_xes("C:/Users/98912/Desktop/Process mining/2/BPI_Challenge_2012/BPI_Challenge_2012.xes")
#dataframe.to_csv("output.csv")

####################### F1-B1-S1
pm4py.view_dotted_chart(dataframe, format='svg')


activity_counts = dataframe['concept:name'].value_counts()
# فرض کنید activity_counts نام یک سری (Series) Pandas با تعداد هر فعالیت باشد
# تنظیمات برای نمایش بهتر
plt.figure(figsize=(10, 6))
plt.bar(activity_counts.index, activity_counts.values, color='blue')
# تنظیمات نمودار
plt.title('event distribution')
plt.xlabel('Activity name')
plt.ylabel('Count')
# چرخاندن نام فعالیت‌ها برای بهبود خوانایی
plt.xticks(rotation=90, ha='right')
# نمایش نمودار
plt.show()




case_counts = dataframe['case:concept:name'].value_counts().reset_index()
case_counts.columns = ['case', 'Count']

# مرتب‌سازی بر اساس مقادیر 'case'
case_counts = case_counts.sort_values(by='case')

# تنظیمات برای نمایش بهتر
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted(case_counts['case']), case_counts['Count'], color='RED')

# تنظیمات نمودار
plt.title('case distribution')
plt.xlabel('case val.')
plt.ylabel('Count')

num_ticks_to_display = 10
step = len(case_counts['case']) // num_ticks_to_display
plt.xticks(range(0, len(case_counts['case']), step), sorted(case_counts['case'][::step]), rotation=45, ha='right')  # ha='right' برای قرار گرفتن لیبل‌ها به خوبی

# اضافه کردن لیبل به هر نوار
for bar in bars:
    yval = bar.get_height()
    if yval >= 5000:
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')

# نمایش نمودار
plt.show()





life_counts = dataframe['lifecycle:transition'].value_counts().reset_index()
life_counts.columns = ['life', 'Count']

# مرتب‌سازی بر اساس مقادیر 'AMOUNT'
life_counts = life_counts.sort_values(by='life')

# تنظیمات برای نمایش بهتر
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted(life_counts['life']), life_counts['Count'], color='RED')

# تنظیمات نمودار
plt.title('life distribution')
plt.xlabel('life val.')
plt.ylabel('Count')

num_ticks_to_display = 3
step = len(life_counts['life']) // num_ticks_to_display
plt.xticks(range(0, len(life_counts['life']), step), sorted(life_counts['life'][::step]), rotation=45, ha='right')  # ha='right' برای قرار گرفتن لیبل‌ها به خوبی

# اضافه کردن لیبل به هر نوار
for bar in bars:
    yval = bar.get_height()
    if yval >= 5000:
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')

# نمایش نمودار
plt.show()





amount_counts = dataframe['case:AMOUNT_REQ'].value_counts().reset_index()
amount_counts.columns = ['AMOUNT', 'Count']

# مرتب‌سازی بر اساس مقادیر 'AMOUNT'
amount_counts = amount_counts.sort_values(by='AMOUNT')

# تنظیمات برای نمایش بهتر
plt.figure(figsize=(10, 6))
bars = plt.bar(sorted(amount_counts['AMOUNT']), amount_counts['Count'], color='RED')

# تنظیمات نمودار
plt.title('AMOUNT distribution')
plt.xlabel('AMOUNT val.')
plt.ylabel('Count')

num_ticks_to_display = 10
step = len(amount_counts['AMOUNT']) // num_ticks_to_display
plt.xticks(range(0, len(amount_counts['AMOUNT']), step), sorted(amount_counts['AMOUNT'][::step]), rotation=45, ha='right')  # ha='right' برای قرار گرفتن لیبل‌ها به خوبی

# اضافه کردن لیبل به هر نوار
for bar in bars:
    yval = bar.get_height()
    if yval >= 5000:
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')

# نمایش نمودار
plt.show()





resource_counts = dataframe['org:resource'].value_counts().reset_index()
resource_counts.columns = ['resource', 'Count']

# مرتب‌سازی بر اساس مقادیر 'AMOUNT'
resource_counts = resource_counts.sort_values(by='resource')

# تنظیمات برای نمایش بهتر
plt.figure(figsize=(15, 6))
bars = plt.bar(resource_counts['resource'], resource_counts['Count'], color='RED')

# تنظیمات نمودار
plt.title('resource distribution')
plt.xlabel('resource name')
plt.ylabel('resource Count')

num_ticks_to_display = 50
step = len(resource_counts['resource']) // num_ticks_to_display
plt.xticks(range(0, len(resource_counts['resource']), step), resource_counts['resource'][::step], rotation=90, ha='right')  # ha='right' برای قرار گرفتن لیبل‌ها به خوبی

# اضافه کردن لیبل به هر نوار
for bar in bars:
    
    yval = bar.get_height()
    if yval >= 5000:
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')

# نمایش نمودار
plt.show()


####################### F1-B1-S2
dataframe.info()
print('Org. resource null Count=', 262200-244190)

####################### F1-B1-S3
df={
    "case_id":[],
    "status": [],
    "sent":   [],
    "amount": []
    }

loan_status= pd.DataFrame(df)

i=0
j=0
caseid=dataframe.iloc[0, 5]
status=''
sent=''
for i in range(262200):
    
    if caseid != dataframe.iloc[i, 5]:
        j+=1

    caseid = dataframe.iloc[i, 5]
    status = dataframe.iloc[i, 2]
    sent = dataframe.iloc[i, 2]
    
    if status == 'A_APPROVED':
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid

              
    if status == 'A_REGISTERED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid

        
    if status == 'A_ACTIVATED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid

        
    if status == 'A_DECLINED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid

        
    if status == 'A_CANCELLED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid

    if sent == 'O_SENT':
        loan_status.at[j, 'sent'] = sent
            
    if sent == 'O_PREPARED':
         loan_status.at[j, 'sent'] = sent
        

loan_status = loan_status.dropna(subset=['case_id', 'status'])
  
APPROVED=0
DECLINED=0
CANCELLED=0
Undecide=0
Osent=0
Onotsent=0

APPROVED = loan_status[loan_status['status'] == "A_APPROVED"].shape[0]
APPROVED += loan_status[loan_status['status'] == "A_REGISTERED"].shape[0]
APPROVED += loan_status[loan_status['status'] == "A_ACTIVATED"].shape[0]
Osent = len(loan_status[(loan_status['status'].isin(["A_REGISTERED", "A_APPROVED", "A_ACTIVATED"])) & (loan_status['sent'].isin(["O_PREPARED", "O_SENT"]))])
Onotsent = APPROVED-Osent
print('APPROVED=',APPROVED)
print('sent=',Osent)
print('not sent=',Onotsent)


DECLINED = loan_status[loan_status['status'] == "A_DECLINED"].shape[0]
Osent = len(loan_status[(loan_status['status'].isin(["A_DECLINED"])) & (loan_status['sent'].isin(["O_PREPARED", "O_SENT"]))])
Onotsent = DECLINED-Osent
print('DECLINED=',DECLINED)
print('sent=',Osent)
print('not sent=',Onotsent)

CANCELLED = loan_status[loan_status['status'] == "A_CANCELLED"].shape[0]
Osent = len(loan_status[(loan_status['status'].isin(["A_CANCELLED"])) & (loan_status['sent'].isin(["O_PREPARED", "O_SENT"]))])
Onotsent = CANCELLED-Osent
print('CANCELLED=',CANCELLED)
print('sent=',Osent)
print('not sent=',Onotsent)

Undecide = 13087-APPROVED-DECLINED-CANCELLED
print('Undecide=', Undecide)


####################### F1-B2-S1

df={
    "case_id":[],
    "status": []
    }

loan_status= pd.DataFrame(df)

i=0
j=0
caseid=dataframe.iloc[0, 5]
status=''
for i in range(262200):
    
    if caseid != dataframe.iloc[i, 5]:
        j+=1

    caseid = dataframe.iloc[i, 5]
    status = dataframe.iloc[i, 2]
    
    if status == 'A_APPROVED':
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid
        
    if status == 'A_REGISTERED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid
        
    if status == 'A_ACTIVATED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid
        
    if status == 'A_DECLINED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid
        
    if status == 'A_CANCELLED' :
        loan_status.at[j , 'status'] = status
        loan_status.at[j, 'case_id'] = caseid
        
OK_loan=0
NOK_loan=0
OK_loan = loan_status[loan_status['status'] == "A_APPROVED"].shape[0]
OK_loan += loan_status[loan_status['status'] == "A_REGISTERED"].shape[0]
OK_loan += loan_status[loan_status['status'] == "A_ACTIVATED"].shape[0]
NOK_loan = loan_status[loan_status['status'] == "A_DECLINED"].shape[0]
NOK_loan += loan_status[loan_status['status'] == "A_CANCELLED"].shape[0]

print('Ok loan=', OK_loan)
print('Not Ok loan=', NOK_loan)
print('Unknown loan=', 13087-OK_loan-NOK_loan)




####################### F1-B2-S2


# فیلتر کردن بر اساس وضعیت مورد نظر (Approved، Canceled، Declined)
filtered_dataframe_approved = dataframe[dataframe['concept:name'] == 'A_APPROVED']
filtered_dataframe_canceled = dataframe[dataframe['concept:name'] == 'O_CANCELLED']
filtered_dataframe_declined = dataframe[dataframe['concept:name'] == 'A_DECLINED']

# ایجاد جدول pivot برای تعداد فعالیت‌ها بر اساس وضعیت و منبع
pivot_table_approved = filtered_dataframe_approved.groupby(['org:resource', 'lifecycle:transition']).size().unstack(fill_value=0)
pivot_table_canceled = filtered_dataframe_canceled.groupby(['org:resource', 'lifecycle:transition']).size().unstack(fill_value=0)
pivot_table_declined = filtered_dataframe_declined.groupby(['org:resource', 'lifecycle:transition']).size().unstack(fill_value=0)

# ادغام جداول بر اساس 'org:resource'
final_table = pd.concat([pivot_table_approved, pivot_table_canceled, pivot_table_declined], axis=1, keys=['Approved', 'Canceled', 'Declined']).fillna(0).astype(int)

# چاپ جدول نهایی
print(final_table)




# ایجاد بازه‌ها
bins = [0, 10000, 20000, 30000, 40000, 50000, 60000]
labels = ['0-10000', '10001-20000', '20001-30000', '30001-40000', '40001-50000', '50001-60000']

# افزودن ستون بازه به دیتافریم
dataframe['amount_range'] = pd.cut(dataframe['case:AMOUNT_REQ'], bins=bins, labels=labels, right=False)

# فیلتر کردن بر اساس وضعیت مورد نظر (Approved، Canceled، Declined)
filtered_dataframe_approved = dataframe[dataframe['concept:name'] == 'A_APPROVED']
filtered_dataframe_canceled = dataframe[dataframe['concept:name'] == 'O_CANCELLED']
filtered_dataframe_declined = dataframe[dataframe['concept:name'] == 'A_DECLINED']

# ایجاد جدول pivot برای تعداد فعالیت‌ها بر اساس وضعیت و بازه مقادیر
pivot_table_approved = filtered_dataframe_approved.groupby(['amount_range', 'concept:name']).size().unstack(fill_value=0)
pivot_table_canceled = filtered_dataframe_canceled.groupby(['amount_range', 'concept:name']).size().unstack(fill_value=0)
pivot_table_declined = filtered_dataframe_declined.groupby(['amount_range', 'concept:name']).size().unstack(fill_value=0)

# تعداد کل کیس‌ها در هر بازه
total_cases_per_range = dataframe.groupby('amount_range')['case:concept:name'].nunique()

# ادغام جداول بر اساس 'amount_range'
final_table = pd.concat([pivot_table_approved, pivot_table_canceled, pivot_table_declined, total_cases_per_range], axis=1, keys=['Approved', 'Canceled', 'Declined', 'Total Cases']).fillna(0).astype(int)

# چاپ جدول نهایی
print(final_table)


####################### F1-B3-S1
case_durations = pm4py.get_all_case_durations(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
sum=0
for i in case_durations:
    sum+=i
print('Throughput time=',sum/(13087*60*60) , 'hours')

pm4py.view_case_duration_graph(dataframe, format='svg', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

####################### F1-B3-S2


dataframe['duration'] = dataframe['time:timestamp'] - dataframe['case:REG_DATE']
# گروه‌بندی بر اساس 'org:resource' و 'case:concept:name' و محاسبه بیشترین زمان برای هر گروه
max_processing_times = dataframe.groupby(['org:resource', 'case:concept:name'])['duration'].max()
# چاپ بیشترین زمان‌ها برای هر منبع و پرونده
print(max_processing_times)
print(max_processing_times.nlargest(10))

average_processing_times = max_processing_times.groupby('org:resource').mean()
# چاپ میانگین زمان‌ها
print(average_processing_times)


max_resource_time = max_processing_times.groupby(['org:resource']).max()
print(max_resource_time)

top_5_resources = max_resource_time.nlargest(5)
print(top_5_resources)






# فیلتر کردن فعالیت‌هایی که با "w" شروع می‌شوند
filtered_dataframe_w = dataframe[dataframe['concept:name'].str.startswith('ٌٌW')]

# گروه‌بندی بر اساس "concept:name" و محاسبه ماکزیمم زمان انجام کار
max_time_for_w_activities = filtered_dataframe_w.groupby('concept:name')['time:timestamp'].max()

# چاپ ماکزیمم زمان‌ها
print(max_time_for_w_activities)







# مرحله‌ی شروع
start_df = dataframe[dataframe['lifecycle:transition'] == 'START']
# مرحله‌ی تکمیل
end_df = dataframe[dataframe['lifecycle:transition'] == 'COMPLETE']
# ایجاد دیتافریم جدید با افزودن مدت زمان به مرحله‌ها
df = start_df.merge(end_df, on=['case:concept:name'])
df['duration'] = df['time:timestamp_y'] - df['time:timestamp_x']
# بدست آوردن شناسه‌ی ردیابی مدت زمان بیشترین اجرا برای هر فرآیند
max_duration_index = df.groupby('case:concept:name')['duration'].idxmax()
# استخراج ردیابی مدت زمان بیشترین اجرا
df_max = df.loc[max_duration_index, ['case:concept:name', 'duration', 'concept:name_x']]
# تغییر نام ستون
df_max.columns = ['case:concept:name', 'max_duration', 'concept:name']
# نمایش نتیجه
print(df_max)

top_5_resources = df_max['max_duration'].nlargest(5)
print(top_5_resources)




###################### F1-B4-S1

#ALPHA MINER
net, im, fm = pm4py.discover_petri_net_alpha(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
bpmn_graph = pm4py.convert_to_bpmn(net, im, fm)
pm4py.view_bpmn(bpmn_graph)

#HEURISTIC MINER
net, im, fm = pm4py.discover_petri_net_heuristics(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
bpmn_graph = pm4py.convert_to_bpmn(net, im, fm)
pm4py.view_bpmn(bpmn_graph)

#INDUCTIVE MINER
bpmn_graph = pm4py.discover_bpmn_inductive(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
pm4py.view_bpmn(bpmn_graph)



from pm4py.statistics.variants.log import get as variants_module
from pm4py.algo.filtering.log.variants import variants_filter
from pm4py.statistics.start_activities.log import get as start_activities_module
from pm4py.statistics.end_activities.log import get as end_activities_module

# Get the variants of the event log
variants = pm4py.get_variants(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

# Get the number of unique variants (sequences of activities)
num_unique_variants = len(variants)

# Get the start activities
# Get the end activities
dfg, start_activities, end_activities = pm4py.discover_dfg(dataframe, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')

# Print or use the obtained simplicity indicators
print("Number of unique variants:", num_unique_variants)
print("Start activities:", start_activities)
print("End activities:", end_activities)

###################### F1-B4-S2

filtered_dataframe_50 = pm4py.filter_variants_top_k(dataframe, 12, activity_key='concept:name', timestamp_key='time:timestamp', case_id_key='case:concept:name')
variant_50 = pm4py.get_variants(filtered_dataframe_50, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
sum=0
for key in variant_50:
    sum+=variant_50[key]
print(sum/13087)

bpmn_graph_50 = pm4py.discover_bpmn_inductive(filtered_dataframe_50, noise_threshold= 0, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
pm4py.view_bpmn(bpmn_graph_50)

###################### F2-B1-S1
rework = pm4py.get_rework_cases_per_activity(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
print(rework)

      

rework_counts = dataframe.groupby(['org:resource','case:concept:name', 'concept:name']).size()
# مشاهده تعداد تکرارها بر اساس تعداد تکرار
top_rework_activities = rework_counts.nlargest(100)
print(top_rework_activities)

# گروه‌بندی بر اساس پرونده و فعالیت و محاسبه تعداد تکرار برای هر جفت پرونده و فعالیت
rework_counts = dataframe.groupby(['case:concept:name', 'concept:name']).size()
# مشاهده تعداد تکرارها بر اساس تعداد تکرار
top_rework_activities = rework_counts.nlargest(100)
print(top_rework_activities)

###################### F2-B1-S2
#سوال تحلیلی

###################### F2-B2-S3
# افزودن ستون مدت زمان اجرای فرآیند به دیتافریم
dataframe['process_duration'] = (dataframe['time:timestamp'] - dataframe['case:REG_DATE']).dt.total_seconds()

# نمودار scatter
plt.figure(figsize=(10, 6))
plt.scatter(dataframe['process_duration'], dataframe['case:AMOUNT_REQ'], alpha=0.1 , s=10)
plt.title('Scatter Plot of Process Duration vs Loan Amount')
plt.xlabel('Process Duration (seconds)')
plt.ylabel('Loan Amount')
plt.tick_params(axis='y', which='both', left=False)
plt.tick_params(axis='x', which='both', bottom=False)

plt.show()

###############








####### F2-B3-S4
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.log import EventLog
from pm4py.algo.clustering.cluster import cluster


filtered_dataframe = pm4py.filter_case_performance(dataframe, 1072732.48 , 11952336.012 , timestamp_key='time:timestamp', case_id_key='case:concept:name')
pm4py.view_events_per_time_graph(filtered_dataframe, format='svg', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
pm4py.view_events_distribution_graph(filtered_dataframe, format='svg', distr_type='days_week', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
pm4py.view_case_duration_graph(filtered_dataframe, format='svg', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

for clust_log in pm4py.cluster_log(filtered_dataframe):
    print(clust_log)

    # تعیین رنگ‌ها بر اساس خوشه‌ها
    
    
    import matplotlib.pyplot as plt
import numpy as np

# تابعی برای تعیین رنگ‌ها بر اساس خوشه‌ها
def get_cluster_colors(labels):
    unique_labels = np.unique(labels)
    color_map = plt.cm.get_cmap('viridis', len(unique_labels))
    cluster_colors = [color_map(label) for label in labels]
    return cluster_colors

# خوشه‌بندی لاگ
clustered_logs = pm4py.cluster_log(filtered_dataframe, sklearn_clusterer=KMeans(n_clusters=num_clusters, random_state=0, n_init="auto"))

# نمایش گراف scatterplot با رنگ‌های خوشه‌ها
plt.figure(figsize=(12, 6))

# انتخاب دو ویژگی برای محورهای x و y (مثال)
x_feature = 'time:timestamp'
y_feature = 'case:concept:name'

# نمایش نقاط با رنگ‌های خوشه‌ها
for cluster_index, clust_log in enumerate(clustered_logs):
    # تبدیل لاگ به دیتافریم
    df = clust_log.to_dataframe()
    
    # استفاده از نام درست برای ستون خوشه‌ها
    cluster_colors = get_cluster_colors(df['cluster'])
    
    plt.scatter(df[x_feature], df[y_feature], c=cluster_colors, s=10, label=f'Cluster {cluster_index + 1}')

plt.xlabel(x_feature)
plt.ylabel(y_feature)
plt.title('Clustering Visualization')
plt.legend()
plt.show()

    
    
    

# گروه‌بندی بر اساس تاریخ شروع پرونده‌ها و شمارش تعداد کیس‌هاimport matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# گروه‌بندی بر اساس تاریخ شروع پرونده‌ها و شمارش تعداد کیس‌ها
case_count_by_timestamp = dataframe.groupby('time:timestamp')['case:concept:name'].count().reset_index()

# تنظیمات نمودار هیستوگرام با seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=case_count_by_timestamp, x='time:timestamp', bins=20, color='blue', edgecolor='black')

plt.title('Distribution of Case Counts over Time')
plt.xlabel('Time')
plt.ylabel('Number of Cases')
plt.grid(True)
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# تنظیمات نمودار هیستوگرام با seaborn
plt.figure(figsize=(12, 6))
sns.histplot(dataframe, x='case:REG_DATE', bins=30, kde=False, color='blue')

plt.title('Histogram of Activity Counts by Registration Time')
plt.xlabel('Registration Time')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

# گروه‌بندی بر اساس منبع و شمارش تعداد کارها
activity_count_by_resource = dataframe.groupby('org:resource')['concept:name'].count().reset_index()

# تنظیمات نمودار میله‌ای با seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=activity_count_by_resource, x='org:resource', y='concept:name', color='blue')

plt.title('Number of Activities by Resource')
plt.xlabel('Resource')
plt.ylabel('Number of Activities')
plt.xticks(rotation=90)  # چرخش لیبل‌ها به زاویه 90 درجه
plt.grid(True)
plt.show()




##########################################
""""
print(dataframe[dataframe['concept:name'] == "W_Wijzigen contractgegevens"])


cycle_time = pm4py.get_cycle_time(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')


pm4py.statistics.rework.cases.log.get.apply(dataframe, activity_key='concept:name', case_id_key='case:concept:name')

process_tree = pm4py.discover_process_tree_inductive(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
pm4py.view_process_tree(process_tree, format='svg')

dfg, start_activities, end_activities = pm4py.discover_dfg(dataframe, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
pm4py.view_dfg(dfg, start_activities, end_activities, format='svg')

performance_dfg, start_activities, end_activities = pm4py.discover_performance_dfg(dataframe, case_id_key='case:concept:name', activity_key='concept:name', timestamp_key='time:timestamp')
pm4py.view_performance_dfg(performance_dfg, start_activities, end_activities, format='svg')

net_ana = pm4py.discover_network_analysis(dataframe, out_column='case:concept:name', in_column='case:concept:name', node_column_source='org:resource', node_column_target='org:resource', edge_column='concept:name')
#pm4py.view_network_analysis(net_ana, format='svg')


net, im, fm = pm4py.discover_petri_net_inductive(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
precision_tbr = pm4py.precision_token_based_replay(dataframe, net, im, fm, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')



#pm4py.view_dotted_chart(dataframe, attributes=['time:timestamp', 'concept:name', 'org:resource'])

metric = pm4py.discover_subcontracting_network(dataframe, resource_key='org:resource', timestamp_key='time:timestamp', case_id_key='case:concept:name')
pm4py.view_sna(metric)


pm4py.view_events_per_time_graph(dataframe, format='svg', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

pm4py.view_events_distribution_graph(dataframe, format='svg', distr_type='days_week', activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

net_ana = pm4py.discover_network_analysis(dataframe, out_column='case:concept:name', in_column='case:concept:name', node_column_source='org:resource', node_column_target='org:resource', edge_column='concept:name')
pm4py.view_network_analysis(net_ana, format='svg')

transition_system = pm4py.discover_transition_system(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
pm4py.view_transition_system(transition_system, format='svg')

prefix_tree = pm4py.discover_prefix_tree(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
pm4py.view_prefix_tree(prefix_tree, format='svg')

net, im, fm = pm4py.discover_petri_net_inductive(dataframe)
aligned_traces = pm4py.conformance_diagnostics_alignments(dataframe, net, im, fm)
pm4py.view_alignments(dataframe, aligned_traces, format='svg')


powl_model = pm4py.discover_powl(dataframe)
pm4py.view_powl(powl_model, format='svg')


variants = pm4py.get_variants(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

variants_tuple = pm4py.get_variants_as_tuples(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')


dataframe = pm4py.format_dataframe(dataframe)
for variant, subdf in pm4py.split_by_process_variant(dataframe):
    print(variant)
    print(subdf)

dataframe = pm4py.format_dataframe(dataframe)
var_paths_durs = pm4py.get_variants_paths_duration(dataframe)
print(var_paths_durs)

msd = pm4py.get_minimum_self_distances(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

msd_wit = pm4py.get_minimum_self_distance_witnesses(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

case_arr_avg = pm4py.get_case_arrival_average(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

rework = pm4py.get_rework_cases_per_activity(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

overlap = pm4py.get_case_overlap(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

cycle_time = pm4py.get_cycle_time(dataframe, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

mean_serv_time = pm4py.get_service_time(dataframe, start_timestamp_key='start_timestamp', aggregation_measure='mean')
print(mean_serv_time)
median_serv_time = pm4py.get_service_time(dataframe, start_timestamp_key='start_timestamp', aggregation_measure='median')
print(median_serv_time)


traces = pm4py.get_frequent_trace_segments(dataframe, min_occ=100)
print(traces)

filtered_dataframe = pm4py.filter_start_activities(dataframe, ['A_ACCEPTED'], activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

filtered_dataframe = pm4py.filter_end_activities(dataframe, ['A_DECLINED'], activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

for clust_log in pm4py.cluster_log(dataframe):
    print(clust_log)

"""


















