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
 '''
    Complete Function Definition
 '''

def GetElectionWinner(votes):
    '''
        Complete Function Definition
    '''


def GetTotalVotes(votes):
    '''
        Complete Function Definition
    '''


def DisplayElectionStatistics(names, votes):
    '''
        Complete Function Defintion
    '''


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
            '''
                Complete code for running Command 1
            '''
        
        elif choice == 2:
            '''
                Complete code for running Command 2
            '''

        elif choice == 3:
            '''
                Complete code for running Command 3
            '''

        elif choice == 4:
            return
        
        print()

           


main()