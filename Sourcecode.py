candidate_1 = input("Enter the 1st candidate name: ")
candidate_2 = input("Enter the 2nd candidate name: ")
print("---------------")
voters_id = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
cand_1 = 0
cand_2 = 0
no_of_voters = len(voters_id)
print("No. of voters:", no_of_voters)
print("---------------")
voted = []
while True:
 if not voters_id:
 print("Voting is over!")
 if cand_1 > cand_2:
 print(f"{candidate_1} won the election with {cand_1} votes.")
 elif cand_2 > cand_1:
 print(f"{candidate_2} won the election with {cand_2} votes.")
 else:
 print("It's a tie!")
58
 break
 else:
 voter = int(input("Enter your voter ID: "))
 if voter in voted:
 print("You already voted!")
 else:
 if voter in voters_id:
 print(f"1. {candidate_1}\n2. {candidate_2}")
 choice = int(input("Enter your choice: "))
 if choice == 1:
 cand_1 += 1
 print(f"You voted for {candidate_1}.")
 print("---------------")
 elif choice == 2:
 cand_2 += 1
 print(f"You voted for {candidate_2}.")
 print("---------------")
 voters_id.remove(voter)
 voted.append(voter)
 else:
 print("You are not allowed to vote.")
 print("---------------")
