import numpy as np
import time
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import pickle

plt.rcParams['figure.figsize'] = [22, 20]
import seaborn as sns

singh = pd.DataFrame()


def datetime_to_float(d):
    return d.timestamp()


startTime = datetime.now()

plt.rcParams['figure.figsize'] = [18, 7]
sns.set(style='whitegrid', palette='muted', font_scale=1.5)

pdf = pd.read_csv('C_sensor.csv', sep="\t")
dflabel = pd.read_csv('C_label.csv', sep="\t")

# only bed and living  common sensors
#sensors = {"PressureBedBedroom": 's1', "PressureSeatLiving": 's2'}



# sensors = {"PIRShowerBathroom": 's1', "PIRBasinBathroom": 's2', "PIRCooktopKitchen": 's3',
#            "MagneticMaindoorEntrance": 's4',
#            "MagneticFridgeKitchen": 's5', "MagneticCabinetBathroom": 's6', "MagneticCupboardKitchen": 's7',
#            "ElectricMicrowaveKitchen": 's8', "ElectricToasterKitchen": 's9', "PressureBedBedroom": 's10',
#            "PressureSeatLiving": 's11', "FlushToiletBathroom": 's12'}

#
# sensors = {"PIRShowerBathroom": 's1', "PIRBasinBathroom": 's2', "PIRDoorKitchen": 's3',"PIRDoorBedroom": 's4',"PIRDoorLiving": 's5',
#            "MagneticMaindoorEntrance": 's6',  "MagneticFridgeKitchen": 's7', "MagneticCupboardKitchen": 's8',
#            "ElectricMicrowaveKitchen": 's9', "PressureBedBedroom": 's10', "PressureSeatLiving": 's11', "FlushToiletBathroom": 's12'}
#


# # #  sensors of kasterenA
# sensors = {"Cups_cupboard": 's1', "Dishwasher": 's2', "Freezer": 's3',"Fridge": 's4', "Frontdoor": 's5',
#            "Groceries_Cupboard": 's6', "Hall-Bathroom_door": 's7',"Hall-Bedroom_door": 's8',
#            "Hall-Toilet_door": 's9', "Microwave": 's10',"Pans_Cupboard": 's11',
#            "Plates_cupboard": 's12',"ToiletFlush": 's13',"Washingmachine": 's14'}
# #A
# #2008-02-25 00:20:14
# #2008-03-23 19:04:47


# sensors={'Bedroom_door': 's1', 'PIR_bedroom': 's2', '_PIR_bathroom': 's3', '_PIR_kitchen': 's4', '_cupboard_groceries': 's5',
#  '_cupboard_plates': 's6', '_fridge': 's7', '_frontdoor': 's8', '_gootsteen_float': 's9', '_mercury_switch_dresser_door': 's10',
#  '_microwave': 's11', '_toaster': 's12', '_toilet_door': 's13', '_toilet_flush': 's14', '_window': 's15', 'balcony_door': 's16',
#  'mercurary_switch_stove_lid': 's17', 'mercury_switch_cutlary_drawer': 's18', 'pressure_mat_bed__right': 's19',
#  'pressure_mat_bed_left': 's20', 'pressure_mat_chair_study': 's21', 'pressure_mat_piano_stool': 's22'}
# # 2009-07-21 13:30:12
# # 2009-08-17 13:49:19

# format_str = "%Y-%m-%d %H:%M:%S"
# t_start = datetime.strptime('2009-07-21 13:30:12', format_str)
# t_end = datetime.strptime('2009-08-17 13:49:19', format_str)#

sensors={'bathroom_swingdoor_left': 's1', 'bathtub_pir_': 's2', 'bed_right_pressure_mat': 's3', 'bedroom_door': 's4',
 'couch_pressure_mat': 's5', 'cupboard_bowl_and_cups': 's6', 'cupboard_herbs_and_platesreed_': 's7',
 'cupboard_pots_and_pans_reed_': 's8', 'cupboard_storage_bins_reed_': 's9', 'cutlary_drawer_mercury_switch': 's10',
 'drawer_with_keys_to_backdoor': 's11', 'dresser_pir_': 's12', 'freezer_reed': 's13', 'fridge_reed_': 's14',
 'frontdoor_reed_': 's15', 'microwave_reed_': 's16', 'pressure_mat_bed_left': 's17', 'sink_upstairs_flush': 's18',
 'toilet_door_downstairs': 's19', 'toilet_flush_downstairs_flush_': 's20', 'toilet_flush_upstairs_flush_': 's21'}
#2008-11-19 22:47:46
# 2008-12-08 08:13:42
format_str = "%Y-%m-%d %H:%M:%S"
t_start = datetime.strptime('2008-11-19 22:47:46', format_str)
t_end = datetime.strptime('2008-12-08 08:13:42', format_str)
# print(datetime.datetime.utcfromtimestamp(int(t_start)).strftime('%Y-%m-%d %H:%M:%S'))
# t_start =t_start+60
# print(datetime.datetime.utcfromtimestamp(int(t_start)).strftime('%Y-%m-%d %H:%M:%S'))

# t_end   = datetime.datetime.strptime('2011-11-28 02:28:59', format_str)+ datetime.timedelta(0, 60)

format_str = "%Y-%m-%d %H:%M:%S"


pdf['Start_time'] =  pd.to_datetime(pdf['Start_time'], format='%Y-%m-%d %H:%M:%S')
pdf['End_time'] =  pd.to_datetime(pdf['End_time'], format='%Y-%m-%d %H:%M:%S')

dflabel['Start_time'] =  pd.to_datetime(dflabel['Start_time'], format='%Y-%m-%d %H:%M:%S')
dflabel['End_time'] =  pd.to_datetime(dflabel['End_time'], format='%Y-%m-%d %H:%M:%S')
# start_list = []
# end_list = []
# for key, row in dflabel.iterrows():
#     start_list += [datetime.strptime(row["Start"] + " " + row["time"], format_str)]
#     end_list += [datetime.strptime(row["End"] + " " + row["time.1"], format_str)]
# dflabel["start_time"] = start_list
# dflabel["end_time"] = end_list
#
# dflabel = dflabel.drop(["Start", "time", "End", "time.1"], axis=1)
#
# start_list = []
# end_list = []
# for key, row in pdf.iterrows():
#     start_list += [datetime.strptime(row["Start"] + " " + row["time"], format_str)]
#     end_list += [datetime.strptime(row["End"] + " " + row["time.1"], format_str)]
# pdf["start_time"] = start_list
# pdf["end_time"] = end_list
#
# pdf = pdf.drop(["Start", "time", "End", "time.1"], axis=1)


sens_values = {}
for key, value in sensors.items():
    sens_values[key] = [[row[0], row[1]]
                        for index, row in pdf.iterrows()
                        if  row[3] == key
                        ]

label = ''
while (t_start <= t_end):
    incT = 60
    feature_vector={}
    label = 'Idle'
    ts = t_start
    print("current time ",t_start)
    fix_wnd = []
    fix_wnd += [[ts - timedelta(minutes=i), ts - timedelta(minutes= i + 1)] for i in range(55)]

    print(fix_wnd)

    for key, value in sensors.items():
        temp_feature_vector = {value + "#" + str(i): 0 for i in range(55)}  #
        # print(temp_feature_vector)
        sensor_intervals = np.array(sens_values[key])
        # print(sensor_intervals)
        s_count = 0
        # print(len(sensor_intervals))
        for sen_intv in sensor_intervals:

            for ind, fix in enumerate(fix_wnd):
                if fix[1] > sen_intv[0] and fix[0] < sen_intv[1]:
                    temp_feature_vector[value + "#" + str(ind)] = 1
                    # print(fix[1],'> ',sen_intv[0],'  ',fix[0],'<',sen_intv[1])
                    # print(fix[1]  >   sen_intv[0],'  ',fix[0]   < sen_intv[1])


        feature_vector.update(temp_feature_vector)
    # print(feature_vector)
    current_time = t_start  # .strftime('%Y-%m-%d %H:%M:%S')
    print("features")
    #     getting label from the label file
    for index1, row1 in dflabel.iterrows():
        if (row1['End_time'] >= current_time >= row1['Start_time']):
            label = row1['activity']
            break

    feature_vector['time'] = current_time
    feature_vector['activity'] = label

    singh = singh.append(pd.DataFrame([feature_vector], columns=feature_vector.keys()), ignore_index=True)
    t_start = t_start + timedelta(seconds=incT)

singh.to_csv('ESTWC.csv', sep='\t', encoding='utf-8')
# singh.to_pickle('singhB240.pkl')    #to save the dataframe, df to 123.pkl
# # df = pd.read_pickle('singhB240.pkl')
print(datetime.now() - startTime)