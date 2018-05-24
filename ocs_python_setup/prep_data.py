import pandas as pd

# create a list of all the file names we want to use
file_names = ['brake_test_area.csv', 'entrance.csv', 'parked_vehicles.csv', 'pits.csv', 'workshop.csv']
# create a pandas DF for each file and put it in a dictionary where the key is the file name (without the ".csv" on the end)
dfs_dict = {tmp_name[:-4]: pd.read_csv(tmp_name, names = ['timestamp', 'PM2.5_nom', 'PM10_nom', 'humidity_percent', 'pm10_ugm3', 'PM10_Avg', 'pm25_ugm3', 'PM2.5_Avg', 'temperature_degC'], index_col='timestamp', header=None, skiprows = 1) for tmp_name in file_names}

# change all the index data types to proper date time stamps and save dataframes as pickles
for data_name in dfs_dict.keys():
    dfs_dict[data_name].index = pd.to_datetime(dfs_dict[data_name].index)
    dfs_dict[data_name] = dfs_dict[data_name][dfs_dict[data_name].index.notnull()]
    dfs_dict[data_name] = dfs_dict[data_name][~dfs_dict[data_name].index.duplicated(keep='first')]
    dfs_dict[data_name].to_pickle(data_name + '.pkl')
