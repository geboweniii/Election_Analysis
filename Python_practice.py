#counties = ["Arapahoe","Denver","Jefferson"]
# counties.append("El Paso")
# counties.insert(2, "Fairfax")
# counties.remove("Denver")
# counties.pop(2)
# counties[0] = "Loudon"
# print(counties)

# counties_tuple = ("Arapahoe","Denver","Jefferson")
# print(counties_tuple[:-1])

# counties_dict = {}
# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438
# print(counties_dict[('Arapahoe')])

# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
# voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.remove({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# print(voting_data)

# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])



# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')



# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')



# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")


# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1



# counties = ["Arapahoe","Denver","Jefferson"]
# for county in counties:
#     print(county)



# print("------------------")
# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)
# print("same result as:")
# for num in range(5):
#     print(num)
# print("------------------")


# counties = ["Arapahoe","Denver","Jefferson"]
# for i in range(len(counties)):
#     print(counties[i])



# counties_tuple = ("Arapahoe","Denver","Jefferson")
# for i in range(len(counties_tuple)):
#       print(counties_tuple[i])
# for county in counties_tuple:
#       print(county)


# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])
# for county in counties_dict:
#     print(counties_dict.get(county))
# for county, voters in counties_dict.items():
#     print(county, voters)
# for county, voters in counties_dict.items():
#     print(voters, county)




# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)
# print("-------------------------")
# for i in range(len(voting_data)):
#       print(voting_data[i])
# print("-------------------------")
# for county in range(len(voting_data)):
#      print(county)
# print("-------------------------")
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# print("-------------------------")
# for county_dict in voting_data:
#      for key, value in county_dict.items():
#          print(value)
# print("-------------------------")
# for county_dict in voting_data:

#      print(county_dict['registered_voters'])


# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")


# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")
# print("-------------------------")
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")


# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)