"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

    # Get the first record from texts
    text_first_record = texts[0]

    # Populate the fields
    # - first column is the incoming tel number
    # - second column is the answering tel number
    incoming_number = text_first_record[0]
    answering_number = text_first_record[1]
    text_time = text_first_record[2]

    print(f"First record of texts, {incoming_number} texts {answering_number} at time {text_time}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    # Get the last record from calls
    calls_last_record = calls[len(calls) - 1]

    # Populate the fields
    # - first column is the incoming tel number
    # - second column is the answering tel number
    # - third column is the start timestamp
    # - fourth column is the call duration
    incoming_number = calls_last_record[0]
    answering_number = calls_last_record[1]
    call_start_time = calls_last_record[2]
    call_duration = calls_last_record[3]

    print(f"Last record of calls, {incoming_number} calls {answering_number} at time {call_start_time}, lasting {call_duration} seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

