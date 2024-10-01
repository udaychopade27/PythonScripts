# list :- data type which can hold multiple values of multiple types
# Array :- data type which can hold multiple values of same type


list_of_clouds=["aws","azure","gcp","ibm"] #create list of clouds

print(list_of_clouds)

list_of_clouds.append("salesforce")
list_of_clouds.append("Alibaba")   #add data to the end of list
print(list_of_clouds)

list_of_clouds.insert(2, "Heroku")  #adds new data at an index we give in command
print(list_of_clouds)
print(len(list_of_clouds))   #this will print length of list

#Iteration of a list
for cloud in list_of_clouds:
    print(cloud)



