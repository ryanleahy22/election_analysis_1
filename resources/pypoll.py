import csv
import os
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:
    txt_file.write("counties in the election\n")
    txt_file.write(("-" * 10) + "\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

   # Read the file object with the reader function.
with open(file_to_load) as election_data:
  
    file_reader = csv.reader(election_data)
       # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)

# Close the file.
txt_file.close()