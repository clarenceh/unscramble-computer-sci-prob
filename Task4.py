"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

# List for all possible telemarketers
telemarketer_list = []

# Set for all numbers that made phone call
caller_set = set()

# Set for all numbers that had either send/receive text or pick up a call
send_receive_text_call_set = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    for text in texts:
        sender_phone_num = text[0]
        receiver_phone_num = text[1]

        # Add to set if not yet in the list
        send_receive_text_call_set.add(sender_phone_num)
        send_receive_text_call_set.add(receiver_phone_num)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        caller_phone_num = call[0]
        receiver_phone_num = call[1]

        # Add to set if not yet exists
        caller_set.add(caller_phone_num)
        send_receive_text_call_set.add(receiver_phone_num)

# Base on caller set and set of numbers that send/receive text and pick up phone call,
# construct the list of possible telemarketers
for phone_num in caller_set:
    if phone_num not in send_receive_text_call_set:
        telemarketer_list.append(phone_num)

# Sort the result list
telemarketer_list.sort()

# Print result
print("These numbers could be telemarketers:")
for phone_num in telemarketer_list:
    print(phone_num)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

