# The task is to help bridge the gap by creating a Python script able to convert 
# employee records to the required format. 

# Import Modules
import os
import csv

# Create path for data file with proper formatting for the operating system
csvpath = os.path.join('.','Resources','employee_data.csv')
output_path = os.path.join('employee_data_reformat.csv')
#print(csvpath)

# Dictionary for US state abbreviations from https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Initialize variables
emp_ID = []
emp_first_name = []
emp_last_name = []
emp_dob = []
emp_ssn = []
emp_state = []

curr_emp_name = []
curr_emp_dob = []
curr_emp_ssn = []

# open csv file as read only
with open(csvpath) as csvfile:

    # CSV reader specifies delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each line of the CSV file
    for line in csvreader:
        # Import the employee_data.csv file, which currently holds employee records like the below:
        #   Emp ID,Name,DOB,SSN,State
        #   214,Sarah Simpson,1985-12-04,282-01-8166,Florida
        #   15,Samantha Lara,1993-09-08,848-80-7526,Colorado
        #   411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
        #print(line)
        emp_ID.append(line[0])

        # The Name column should be split into separate First Name and Last Name columns.
        curr_emp_name = line[1].split(' ')
        emp_first_name.append(curr_emp_name[0])
        emp_last_name.append(curr_emp_name[1])
        
        #print(curr_emp_name)

        # The DOB data should be re-written into MM/DD/YYYY format.
        curr_emp_dob = line[2].split("-")
        dob_reformat = curr_emp_dob[1] + "/" + curr_emp_dob[2] + "/" + curr_emp_dob[0]
        emp_dob.append(dob_reformat)
        #print(dob_reformat)

        # The SSN data should be re-written such that the first five numbers are hidden from view.
        curr_emp_ssn = line[3].split("-")
        ssn_reformat = "***-**-" + curr_emp_ssn[2]
        emp_ssn.append(ssn_reformat)
        #print(curr_emp_ssn)

        # The State data should be re-written as simple two-letter abbreviations.
        curr_emp_state = line[4]
        if curr_emp_state in us_state_abbrev:
            emp_state.append(us_state_abbrev[curr_emp_state])
        else:
            print(f"{emp_state} not in dictionary")

# Then convert and export the data to use the following format instead:
#   Emp ID,First Name,Last Name,DOB,SSN,State
#   214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#   15,Samantha,Lara,09/08/1993,***-**-7526,CO
#   411,Stacy,Charles,12/20/1957,***-**-8526,PA

# Zip all three lists together into tuples
roster = zip(emp_ID, emp_first_name, emp_last_name, emp_dob, emp_ssn, emp_state)

# open the output file, create a header row, and then write the zipped object to the csv
# newline added to account for windows printing a blank line between each row
with open(output_path, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    writer.writerows(roster)

print(f"Thank you for converting your data using PyBoss, your results are in the file {output_path}")