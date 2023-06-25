import os
import csv

# Define the folder paths
normal_folder = 'C://Users//LENOVO//Documents//Python Scripts//Pathole_and_humps_detection//Datasets//Humps'
humps_folder = 'C://Users//LENOVO//Documents//Python Scripts//Pathole_and_humps_detection//Datasets//normal'
pothole_folder = 'C://Users//LENOVO//Documents//Python Scripts//Pathole_and_humps_detection//Datasets//potholes'

data = []

for filename in os.listdir(normal_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  
        row = [filename, 1, 0, 0]  
        data.append(row)

for filename in os.listdir(humps_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  
        row = [filename, 0, 1, 0]  
        data.append(row)

for filename in os.listdir(pothole_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  
        row = [filename, 0, 0, 1]  
        data.append(row)

csv_file = 'output.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['imagename', 'normal', 'humps', 'pothole'])  
    writer.writerows(data)  

print("File has been created successfully.")
