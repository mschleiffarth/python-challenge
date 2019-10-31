import csv

csvpath = "Resources/election_data.csv"

totalVotes = 0
candidates = ["empty"]
votes = [0]
voteCast = False
mostVotes = 0
winner = "nobody"

with open(csvpath, newline='') as csvfile:

    electionData = csv.reader(csvfile, delimiter=',')

    csv_header = next(electionData)
    

    for row in electionData:
        voteCast = False
        totalVotes += 1

        if(candidates[0] == "empty"):
            candidates[0] = row[2]
            votes [0] = 1
        else:
            for i in range(len(candidates)):
                if(row[2] == candidates[i]):
                    votes [i] += 1
                    voteCast = True
                    break
            if (voteCast == False):
                candidates.append(str(row[2]))
                votes.append(1)
    
with open("output.txt", "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write("Total Votes: " + str(totalVotes) + "\n")
    output_file.write("----------------------------\n")
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(totalVotes))
    print("----------------------------")
        
    for i in range(len(candidates)):
        output_file.write(str(candidates[i]) + ": " + str(round(100 * (float(votes[i])/float(totalVotes)), 3)) + "% (" + str(votes[i]) + ")\n")
        print(str(candidates[i]) + ": " + str(round(100 * (float(votes[i])/float(totalVotes)), 3)) + "% (" + str(votes[i]) + ")")


    for i in range(len(candidates)):
        if(votes[i] > mostVotes):
            mostVotes = int(votes[i])
            winner = str(candidates[i])

    output_file.write("----------------------------\n")
    print("----------------------------")
    output_file.write("Winner: " + winner + "\n")
    print("Winner: " + winner)
    output_file.write("----------------------------\n")
    print("----------------------------")
    output_file.close()