import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
#OLD HORRIBLE SOLUTION
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#OLD RUNTIME
# 64 duplicates:
# runtime: 19.01556921005249 seconds

#introducing new variables and methods

#sooooooooo..... I decided to just do sort.. and it made things nicer.........
#I thought about the robot sorting the number maze and this gave me the idea to reset the lists using sort, 
# just like numbers and then iterating it in a numberly fashion appending the duplicates
names_1.sort()
names_2.sort()

#made parameters for current positioning 
x = 0
y = 0

#while both x and y are smaller than the lists
while x < len(names_1) and y < len(names_2):

    #when params x matches y,  
    if names_1[x] == names_2[y]:
        #the chosen name will now be appended  
        duplicates.append(names_1[x])
        #then the lists will move to new position
        x += 1
        y += 1
    #if positions are uneven    
    elif names_1[x] < names_2[y]:
    #one will add to itself     
        x += 1
    #or the other will add to itself    
    else:
        y += 1    

#new runtime
#64 duplicates:
#runtime: 0.05090212821960449 seconds


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
