import pandas as pd
import plotly.figure_factory as ff
import statistics as st

import csv

df = pd.read_csv("performance.csv")
Datalist = df["reading score"].to_list()
h_mean = st.mean(Datalist)
h_median = st.median(Datalist)
h_mode = st.mode(Datalist)
h_std = st.stdev(Datalist)
print("mean,median,mode of data is {},{},{} respectively".format(h_mean,h_median,h_mode))
h_first_std_deviation_start,h_first_std_deviation_end = h_mean-h_std,h_mean+h_std
h_second_std_deviation_start,h_second_std_deviation_end = h_mean-(2*h_std),h_mean+(2*h_std)
h_third_std_deviation_start,h_third_std_deviation_end = h_mean-(3*h_std),h_mean+(3*h_std)
h_list_of_data_within_1_std_deviation = [result for result in Datalist if result>h_first_std_deviation_start and result<h_first_std_deviation_end]
h_list_of_data_within_2_std_deviation = [result for result in Datalist if result>h_second_std_deviation_start and result<h_second_std_deviation_end]
h_list_of_data_within_3_std_deviation = [result for result in Datalist if result>h_third_std_deviation_start and result<h_third_std_deviation_end]
print("{} % of data lies within first standard deviation of height".format(len(h_list_of_data_within_1_std_deviation)*100.0/len(Datalist)))
print("{} % of data lies within second standard deviation of height".format(len(h_list_of_data_within_2_std_deviation)*100.0/len(Datalist)))
print("{} % of data lies within third standard deviation of height".format(len(h_list_of_data_within_3_std_deviation)*100.0/len(Datalist)))
print("standard deviation of the height is {} ".format(h_std))
