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
def get_election_winner(votes):
  max_votes = max(votes)
  winner_index = votes.index(max_votes)

  return winner_index


#GET TOTAL VOTES
def get_total_votes(votes):
  total = 0
  for i in votes:
    total += i
  
  return total


#DISPLAY ELECTION STATISTICS
def displaY_election_statistics(candidates, votes):
  tot_vote = sum(votes)
  num_candidates = len(candidates)

  print('Candidate\tVotest\tPercentage')
  print('-----------------------------------')

  for i in range(num_candidates):
    percent = (votes[i] / total_votes) * 100
    
    print(f'{candidates[i]}\t{votes[i]}\t{percentage:.2f}%')

  print('-----------------------------------')
  print(f'Total votes cast: {total_votes}')
  print(f'Average votes per candidate: {total_votes / num_candidates:.2f}')


#EXIT PROGRAM
