
# in every minute that we started from the first activity (2011-11-28 02:27:59') we read all sensors time interval from the
# frist day-activity to the last day-activity and then we apply  15 fuzzy temporal windows that we created based on the Fibonanci values
# (look at below to see the Fibonanci array) so each fuzzy temporal window has 4 values l1,u1,u2,l2 so we apply a fuzzy windwo on all time
# intervals of a sensors then we select the highest value to put as a first future of the sensor so for each sensors we have 15 features
# (number of fuzzy temporal windows) then we apply the second fuzzy temporal window on all the sensors intervals to make the second feature
# value and then we continue untill we apply 15 fuzzy temporal windows on all the sensor time intervals and then we do the same process on all
# other seonsors time interval.

# feb=[-0, -0, -1,-1,-2, -3, -5, -8, -13, -21, -34, -55, -89, -144, -233, -377, -610, -987]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# import datetime
import time
# %matplotlib inline
from datetime import datetime, timedelta

startTime = datetime.now()

# In[90]:


plt.rcParams['figure.figsize'] = [18, 7]
sns.set(style='whitegrid', palette='muted', font_scale=1.5)

pdf=pd.read_csv('B_sensor.csv', sep='\t')
dflabel = pd.read_csv('B_label.csv', sep='\t')

# pdf.to_csv('pdf.csv', sep='\t', encoding='utf-8')


def datetime_to_float(d):
    return d.timestamp()

# this function computes the membership degree of the fuzzy windows

def comput_degree1(l1, u1):  # for case 2
    try:
        m = float(1) / float((u1 - l1))
        n = float(-l1) / float((u1 - l1))
    except ZeroDivisionError:
        return 0, 0

    return m, n


def comput_degree2(l2, u2):  # for case 5
    try:
        m = 1 / float((l2 - u2))
        n = -u2 / float((l2 - u2))
    except ZeroDivisionError:
        return 0, 0
    return m, n


def evalFTW(l1, u1, u2, l2, t0, tN):
    if (tN < l1):  # case 1
        return 0
    elif (l1 <= tN <= u1):  # case 2
        m, n = comput_degree1(l1, u1)
        #         print(m*tN+n)
        return (m * tN + n)

    elif (t0 < l1 and u1 <= tN <= u2):  # case 3
        return 1

    elif (t0 > l2):  # case 4
        return 0

    elif (u2 <= t0 <= l2):  # case 5
        m, n = comput_degree2(l2, u2)
        return (m * t0 + n)
    elif (u1 <= t0 <= u2 and tN > l2):  # case 6
        return 1
    elif (l1 <= t0 <= u1 and u2 < tN < l2):  # case 7
        return 1
    elif (l2 >= t0 >= u2 and tN < l2):  # case 8
        m, n = comput_degree2(l2, u2)
        return (m * t0 + n)
    elif (l2 >= tN >= u2 and t0 > u2):  # case 9
        m, n = comput_degree1(l2, u2)
        return (m * tN + n)
    else:
        return 1  # This is not given in the pictures (FTW) but I put this here otherwise we get NON which means that sometimes we have a value that does not belong to the above cases.





# #  sensors of kasterenA
# sensors = {"Cups_cupboard": 's1', "Dishwasher": 's2', "Freezer": 's3',"Fridge": 's4', "Frontdoor": 's5',
#            "Groceries_Cupboard": 's6', "Hall-Bathroom_door": 's7',"Hall-Bedroom_door": 's8',
#            "Hall-Toilet_door": 's9', "Microwave": 's10',"Pans_Cupboard": 's11',
#            "Plates_cupboard": 's12',"ToiletFlush": 's13',"Washingmachine": 's14'}
#A
#2008-02-25 00:20:14
#2008-03-23 19:04:47

# Sensors of kasteren B

sensors={'Bedroom_door': 's1', 'PIR_bedroom': 's2', '_PIR_bathroom': 's3', '_PIR_kitchen': 's4', '_cupboard_groceries': 's5',
 '_cupboard_plates': 's6', '_fridge': 's7', '_frontdoor': 's8', '_gootsteen_float': 's9', '_mercury_switch_dresser_door': 's10',
 '_microwave': 's11', '_toaster': 's12', '_toilet_door': 's13', '_toilet_flush': 's14', '_window': 's15', 'balcony_door': 's16',
 'mercurary_switch_stove_lid': 's17', 'mercury_switch_cutlary_drawer': 's18', 'pressure_mat_bed__right': 's19',
 'pressure_mat_bed_left': 's20', 'pressure_mat_chair_study': 's21', 'pressure_mat_piano_stool': 's22'}
# 2009-07-21 13:30:12
# 2009-08-17 13:49:19
format_str = "%Y-%m-%d %H:%M:%S"
t_start = datetime.strptime('2009-07-21 13:30:12', format_str)
t_end = datetime.strptime('2009-08-17 13:49:19', format_str)
t_start = time.mktime(t_start.timetuple()) + 1 * 60 * 60   # GMT+1
t_end = time.mktime(t_end.timetuple()) + 1 * 60 * 60

print(t_start)
# print(datetime.datetime.utcfromtimestamp(int(t_start)).strftime('%Y-%m-%d %H:%M:%S'))
# t_start =t_start+60
# print(datetime.datetime.utcfromtimestamp(int(t_start)).strftime('%Y-%m-%d %H:%M:%S'))

# t_end   = datetime.datetime.strptime('2011-11-28 02:28:59', format_str)+ datetime.timedelta(0, 60)

# feb = [-0, -0, -1, -1, -2, -3, -5, -8, -13, -21, -34, -60] # one hour it will create 9 windows
feb=[-0, -0, -1,-1,-2, -3, -5, -8, -13, -21, -34, -55, -89, -144, -233, -377, -610, -987] # 16.45 hours it will create 15 windows

pdf['Start_time'] =  pd.to_datetime(pdf['Start_time'], format='%Y-%m-%d %H:%M:%S')
pdf['End_time'] =  pd.to_datetime(pdf['End_time'], format='%Y-%m-%d %H:%M:%S')

dflabel['Start_time'] =  pd.to_datetime(dflabel['Start_time'], format='%Y-%m-%d %H:%M:%S')
dflabel['End_time'] =  pd.to_datetime(dflabel['End_time'], format='%Y-%m-%d %H:%M:%S')

# format_str = "%Y-%m-%d %H:%M:%S"
# start_list = []
# end_list = []
# for key, row in dflabel.iterrows():
#     start_list += [datetime.strptime(row["Start_time"], format_str)]
#     end_list += [datetime.strptime(row["End_time"], format_str)]
# dflabel["start_time"] = start_list
# dflabel["end_time"] = end_list
#
#
# dflabel=dflabel.drop(["Start", "time", "End", "time.1"], axis=1)
#
# for index, row in pdf.iterrows():
#     print(row[0] + ' ' + row[1])
#
# format_str = "%Y-%m-%d %H:%M:%S"
# start_list = []
# end_list = []
# for key, row in pdf.iterrows():
#     start_list += [datetime.strptime(row["Start"] + " "+ row["time"], format_str)]
#     end_list += [datetime.strptime(row["End"] + " " + row["time.1"], format_str)]
# pdf["start_time"] = start_list
# pdf["end_time"] = end_list
#
# pdf=pdf.drop(["Start", "time", "End", "time.1"], axis=1)


sens_values={}
for key, value in sensors.items():
    sens_values [key] = [ [row[0], row[1]]
                         for index, row in pdf.iterrows()
                         if  row[3] == key
                        ]

print(pdf.info())
print(dflabel.info())

label = ''
dataset = pd.DataFrame()
while (t_start <= t_end):

    incT = 60

    feature_vector = {}
    label = 'Idle'
    for key, value in sensors.items():

        sensor_intervals = np.array(sens_values[key])
        print(sensor_intervals)
        s_count = 0
        print(len(sensor_intervals))


        for i in range(15):  #we have 9 fuzzy temporal window and apply them on each single interval
            ts = t_start
            l1 = ts + incT * feb[i]
            u1 = ts + incT * feb[i + 1]
            u2 = ts + incT * feb[i + 2]
            l2 = ts + incT * feb[i + 3]

            degrees = [ evalFTW(l2, u2, u1, l1, datetime_to_float(sen_intv[0]),  datetime_to_float(sen_intv[1]))
                        for sen_intv in sensor_intervals
                       ]
            print(degrees)
            s_ftw_degree = max(degrees)
            feature_vector[value + "#" + str(s_count)] = s_ftw_degree

            s_count += 1


    current_time = datetime.utcfromtimestamp(int(t_start))  # .strftime('%Y-%m-%d %H:%M:%S')
    #     getting label from the label file
    for index1, row1 in dflabel.iterrows():
        if (row1['End_time'] >= current_time >= row1['Start_time']):
            label = row1['activity']
            break


    feature_vector['time'] = current_time
    feature_vector['activity'] = label

    dataset = dataset.append(pd.DataFrame([feature_vector], columns=feature_vector.keys()), ignore_index=True)
    t_start = t_start + incT


dataset.to_csv('KasB_15wind.csv', sep='\t', encoding='utf-8')


#######################################################################################


print(datetime.now() - startTime)