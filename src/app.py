import os
import json
import numpy as np

input_directory = os.environ['IEXEC_IN']
output_directory = os.environ['IEXEC_OUT']
input_filename = os.environ['IEXEC_DATASET_FILENAME']

filepath = os.path.join(input_directory, input_filename)
print("Loading file " + filepath)

sorted_array = []
if os.path.exists(filepath):
    file_data = np.loadtxt(filepath, dtype=float)
    print("File loaded")
    sorted_array = np.sort(file_data, kind='mergesort')
    print("Array sorted")

np.savetxt(os.path.join(output_directory, "sorted_array.txt"), sorted_array)
print("File saved")

with open(os.path.join(output_directory, "computed.json"), 'w+') as f:
    json.dump(
        {"deterministic-output-path": os.path.join(output_directory, "sorted_array.txt")}, f)
