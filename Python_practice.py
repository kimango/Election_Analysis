print("Hello World")
my_list = list()
print(my_list)
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0:2])
print(counties[0:1])
print(counties[1:])
len(counties)
print(len(counties))
counties.append("El_Paso")
print(counties)
counties.insert(2, "El_Paso")
print(counties)
counties.remove("El_Paso")
print(counties)
counties.pop(3)
print(counties)
my_tuple =(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
len(counties_tuple)
my_dictionary ={}
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
len(counties_dict)
print(len(counties_dict))
counties_dict.items()
print(counties_dict.items())
counties_dict.keys()
print(counties_dict.keys())
counties_dict.values()
print(counties_dict.values())
counties_dict.get("Denver")
print(counties_dict.get("Denver"))

voting_data= []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

for county in counties:
    print(county) 

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)  

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):
    print(voting_data[county]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
     print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = ("You received {candidate_votes} number of votes. "
"The total number of votes in the election was {total_votes}. "
"You received {candidate_votes / total_votes * 100} % of the total votes.")
print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")


