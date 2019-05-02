"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


def is_bangalore_num(tel_num):
    """
    Chcek whether a tel number is Bangalore fix line
    :param tel_num:
    :return: boolean
    """
    result = False

    if tel_num.startswith("(080)"):
        result = True

    return result


def get_area_code_mobile_prefix(tel_num):
    """
    Get the area code or mobile prefix from a tel number
    :param tel_num:
    :return: area code or mobile prefix. None if not found
    """

    area_code_mobile_prefix = None

    if tel_num[0] == '(':       # Fix line with area code in bracket
        area_code_mobile_prefix = tel_num[1: tel_num.find(")")]
    elif tel_num[5] == ' ':     # Mobile no have a space in it
        first_four_digits = tel_num[0:4]

        # Check prefix in 7, 8, 9
        if first_four_digits[0] in ['7', '8', '9']:
            area_code_mobile_prefix = first_four_digits
    elif tel_num.isdigit():
        first_three_digits = tel_num[0:3]

        # Check whether it's 140
        if first_three_digits == '140':
            area_code_mobile_prefix = first_three_digits

    return area_code_mobile_prefix


# List of all unique area code/mobile prefix called by Bangalore numbers
area_code_by_bangalore_list = []

# Total calls from Bangalore
total_calls_from_bangalore = 0

# Total calls from Bangalore to Bangalore
total_calls_from_bangalore_to_bangalore = 0

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    for call in calls:
        # Retrieve the incoming number and check whether it's from Bangalore
        incoming_phone_num = call[0]

        is_from_bangalore = is_bangalore_num(incoming_phone_num)

        if is_from_bangalore:
            total_calls_from_bangalore += 1

            # Retrieving the receiving phone number
            receiving_phone_number = call[1]

            # Check whether receiving number is a Bangalore number
            is_to_bangalore = is_bangalore_num(receiving_phone_number)

            if is_to_bangalore:
                total_calls_from_bangalore_to_bangalore += 1

            area_code_mobile_prefix = get_area_code_mobile_prefix(receiving_phone_number)

            # Add to the result list if not exist
            if area_code_mobile_prefix and area_code_mobile_prefix not in area_code_by_bangalore_list:
                area_code_by_bangalore_list.append(area_code_mobile_prefix)

# Sort the result list for Task 3 Part A
area_code_by_bangalore_list.sort()

# Print result for Task 3 Part A
print("The numbers called by people in Bangalore have codes:")
for area_code in area_code_by_bangalore_list:
    print(area_code)

# Calculate Task 3 Part B and print result
to_bangalore_calls_percentage = total_calls_from_bangalore_to_bangalore / total_calls_from_bangalore * 100
print('{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(to_bangalore_calls_percentage))

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
