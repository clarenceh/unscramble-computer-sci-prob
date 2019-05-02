"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# List of unique phone number and the total time spent in calls
phone_num_to_time_spent_dict = {}

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    # For each call, update the dict with the incoming/receiving phone number with the length of call
    # Assume that both phone numbers spent the same time in call
    for call in calls:
        incoming_phone_num = call[0]
        receiving_phone_num = call[1]
        call_time = int(call[3])  # Convert call time to int

        if incoming_phone_num not in phone_num_to_time_spent_dict:
            phone_num_to_time_spent_dict[incoming_phone_num] = call_time
        else:
            phone_num_to_time_spent_dict[incoming_phone_num] += call_time

        if receiving_phone_num not in phone_num_to_time_spent_dict:
            phone_num_to_time_spent_dict[receiving_phone_num] = call_time
        else:
            phone_num_to_time_spent_dict[receiving_phone_num] += call_time

# Fine the telephone num with max value
max_time_spent_tel_num = max(phone_num_to_time_spent_dict, key=phone_num_to_time_spent_dict.get)
max_time_spent = phone_num_to_time_spent_dict[max_time_spent_tel_num]
print(f"{max_time_spent_tel_num} spent the longest time, {max_time_spent} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
