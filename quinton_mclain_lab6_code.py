'''
Author: Quinton McLain
Program Title: Election Statistics
File Description:
This program will help Barry at the local election office
'''

def load_data(file_name):
    file = open(file_name, "r")

    candidates = []
    votes = []

    line = file.readline()

    while(line != ''):
        candidate, vote_count = line.split(",")
        candidates.append(candidate)
        votes.append(int(vote_count))
        line = file.readline()

    file.close()

    return candidates, votes

def LookupCandidateCount(search_name, names, votes):
  for i in range(len(names)):
    if names[i]== search_name:
      return votes[i]
  return -1

def GetElectionWinner(votes):
  max_votes = max(votes)
  winner_index = votes.index(max_votes)

  return winner_index



def GetTotalVotes(votes):
  total = 0
  for i in votes:
    total += i
  
  return total

def DisplayElectionStatistics(names, votes):
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



def main():
    candidates, votes = load_data("candidate_votes.txt")
    
    choice = -1
    
    while choice != 4:
        print("Main Menu")
        print("1. Candidate Count Lookup")
        print("2. Get Election Winner")
        print("3. Display Election Statistics")
        print("4. Exit Program")

        choice = int(input("--: "))

        while(choice < 1 or choice > 4):
            choice = int(input("Error: Invalid input.  --: "))

        print()

        if(choice == 1):
          search_name = input("Enter candidate's last name: ")
          LookupCandidateCount(search_name, candidates, votes)
          if count != -1:
            print(f'{search_name} recieved {count} votes')
          else:
            print(f'No candidate with the last name {search_name} found.')
        
        elif choice == 2:
          winner_index = GetElectionWinner(votes)
          print(f'The winnder of the election is {candidates[winner_index]}')

        elif choice == 3:
            DisplayElectionStatistics(candidates, votes)

        elif choice == 4:
            return
        
        print()

           


main()
