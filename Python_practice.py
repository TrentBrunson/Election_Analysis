print("Hello World!")

counties = ["arapahoe","denver","jefferson"]
print(counties)

if counties[1]=='denver':
    print(counties[1])

if counties[1] != 'jefferson':
    print(counties[:])

temperature=int(input("What is the temperature outside? "))
if temperature>82:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90 and score <= 100:
    print('Your grade is an A.')
elif score >100:
    print('You got an A+!!!')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

if "arapahoe" in counties:
    print("True") 
else:
    print("False")

if "El Paso" not in counties:
    print("True") 
else:
    print("False")

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")   

x = 5
y = 5
if x == 5 and y == 5:
    print("True") 
else:
    print("False")

if x == 3 or y == 5:
    print("True")
else:
    print("False")

if not(x > y):
    print("True") 
else:
    print("False")

if "arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


if "arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

x = 0
while x < 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
print()

for num in range(2):
    print(num)
    print ()

for i in range(len(counties)):
    print(counties[i])

counties_tuple = ("Arapahoe","Denver","Jefferson")

for county in counties_tuple:
      print(county)
for i in range(len(counties_tuple)):
      print(counties_tuple[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print()
for county in counties_dict:
    print(county)
print()

for county in counties_dict.keys():
    print(county)

print()

for voters in counties_dict.values():
    print(voters)
print()

for i in counties_dict:
    print(counties_dict[i])
print()

for county, voters in counties_dict.items():
    print(county, voters)
    print()

for county, voters in counties_dict.items():
    print(county +' county has '+ str(voters) +' registered voters.')
    print()
print()

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

print()

for county in range(len(voting_data)):
     print(county)

for i in range(len(voting_data)):
      print(voting_data[i])

print()

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
print()

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
print()

print (voting_data)
for county_dict in voting_data:  

     print(county_dict.values())
print()
for county_dict in voting_data:    

   for value in county_dict:      

       print(value)
print()
for county_dict in voting_data:

     for key, value in county_dict.items():

         print(value)
print()
for county_dict in voting_data:
     print(county_dict['registered_voters'])
     print(county_dict['county'])
print()

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes/total_votes * 100}% or the total votes.")
print()

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
print()

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

print()
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.") 
print()

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.") 
print()

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

print()

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
now = now.strftime('%M, %D, %H, %S')

# format(now, '.1f')
# Print the present time.
print("The time right now is ", now) #how to limit this to 1 decimal place???

