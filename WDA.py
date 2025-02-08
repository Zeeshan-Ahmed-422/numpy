
# # data = np.genfromtxt(r'C:\Users\DELL\Documents\weather_data.csv', delimiter=',', skip_header=1)
import numpy as np

# # Replace this with the correct path to your weather_data.csv file
data = np.genfromtxt(r'C:\Users\DELL\Desktop\Python\weather_data.csv', delimiter=',', skip_header=1)
# import numpy as np

# Absolute path to the weather_data.csv file
# data = np.genfromtxt(r'C:\Users\DELL\Desktop\weather_data.csv', delimiter=',', skip_header=1)



print(data)
# import os
# print(os.getcwd())
# import os
# file_path = r'C:\Users\DELL\Desktop\Python\weather_data.csv'

# # Check if Python can read the file
# with open(file_path, 'r') as file:
#     content = file.readlines()
#     print("File Content:")
#     print(content)


# Check the current working directory
# print("Current Working Directory:", os.getcwd())

# Check if the file exists in the directory
# print("Does the file exist?", os.path.exists('weather_data.csv'))