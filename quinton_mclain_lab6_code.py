'''
Author: Quinton McLain
Program Title: Election Statistics
File Description:
This program will help Barry at the local election office
'''

#CANDIDATE VOTE COUNT LOOKUP
def candidate_lookup(search_name, names, votes):
  for i in range(len(names)):
    if names[i]== search_name:
      return votes[i]
  return -1

#GET ELECTION WINNER


#DISPLAY ELECTION STATISTICS



#EXIT PROGRAM