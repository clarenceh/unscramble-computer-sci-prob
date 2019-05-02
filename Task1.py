"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

# Set to store unique telephone  numbers
tel_num_set = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text_record in texts:
        incoming_phone_num = text_record[0]
        receiving_phone_num = text_record[1]

        tel_num_set.add(incoming_phone_num)
        tel_num_set.add(receiving_phone_num)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call_record in calls:
        incoming_phone_num = call_record[0]
        receiving_phone_num = call_record[1]

        tel_num_set.add(incoming_phone_num)
        tel_num_set.add(receiving_phone_num)

# The number of elements in the list is the no. of different telephone numbers
no_of_unique_phone_num = len(tel_num_set)

print(f"There are {no_of_unique_phone_num} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
