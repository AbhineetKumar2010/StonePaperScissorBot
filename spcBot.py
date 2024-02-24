shoot = str(input("Choose\n1)Rock\n2)Paper\n3)Scissor\n -->")) #getting the choice of the player

if shoot == "1" or shoot == "Rock" or shoot == "rock": #calculating or basically checking the response and playing the best move against it
    print("Paper")
    input()
elif shoot == "2" or shoot == "Paper" or shoot == "paper":
    print("Scissor")
    input()
elif shoot == "3" or shoot == "Scissor" or shoot == "scissor":
    print("Rock") 
    input()
else:
    print("Your choice may be wrong or you have maybe made a mistake in the spelling.")
