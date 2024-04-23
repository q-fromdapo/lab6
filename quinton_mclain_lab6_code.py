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
        if names[i] == search_name:
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
    num_candidates = len(names)

    max_name_length = max(len(name) for name in names)
    column1_width = max(max_name_length, len("Candidate"))
    column2_width = len("Votes")
    column3_width = len("Percentage")

    print(f'{"Candidate":<{column1_width}} {"Votes":<{column2_width}} {"Percentage":<{column3_width}}')
    print('-' * (column1_width + column2_width + column3_width + 4))

    for i in range(num_candidates):
        percent = (votes[i] / tot_vote) * 100
        print(f'{names[i]:<{column1_width}} {votes[i]:<{column2_width}} {percent:.2f}%')

    print('-' * (column1_width + column2_width + column3_width + 4))
    print(f'Total votes cast: {tot_vote}')
    print(f'Average votes per candidate: {tot_vote / num_candidates:.2f}')

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

        if choice == 1:
            search_name = input("Enter candidate's last name: ")
            candidate_votes = LookupCandidateCount(search_name, candidates, votes)
            if candidate_votes != -1:
                print(f'{search_name} received {candidate_votes} votes')
            else:
                print(f'No candidate with the last name {search_name} found.')
        
        elif choice == 2:
            winner_index = GetElectionWinner(votes)
            print(f'The winner of the election is {candidates[winner_index]}')

        elif choice == 3:
            DisplayElectionStatistics(candidates, votes)

        elif choice == 4:
            return
        
        print()

main()


