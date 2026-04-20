#Intro
print('🎩 WELCOME, DEAR PLAYER!🎪')
print('I’m Caine! Your charming, dazzling, question-asking ringmaster!🎈')
print('Step right up and test your supposed expertise of the Digital Circus!')
print('No cheating… or I’ll have to get creative 😄')

playing = input("Today's adventure is...A Quizzling Quiz! Ready to play? ")

if playing.lower() != 'yes':
    print('WHY DO YOU PEOPLE TORMENT ME?')
    quit()

print("Well, let's not waste any time! Let's get right into the show!")
score = 0


# Question 1
answer = input('What is the name of the main human character we follow? ')
if answer.lower() == 'pomni':
    print('Correct! That was an easy one though.')
    score += 1
else:
    print('Incorrect! You spiral into existential dread immediately!')

# Question 2
answer = input('What is the ringmaster’s name? ')
if answer.lower() == 'caine':
    print('Correct! Oh, I do love attention!')
    score += 1
else:
    print('Incorrect! You got sent to the void!')

# Question 3
answer = input('What is the name of the masked character who struggles emotionally? ')
if answer.lower() in ['gangle', 'jax']:
    print('Correct! High five!')
    score += 1
else:
    print("Incorrect! You break Gangle's mask")

# Question 4
answer = input('What is the chaotic rabbit character’s name? ')
if answer.lower() == 'jax':
    print('Correct! He’s not very nice, is he?')
    score += 1
else:
    print('Incorrect! Jax pranked you… permanently!')

# Question 5 (deeper)
answer = input('What state do characters enter when they lose their sanity? ')
if answer.lower() == 'abstraction':
    print('Correct! Let’s hope you avoid that!')
    score += 1
else:
    print('Incorrect! You abstracted!')


# Question 6 (lore)
answer = input('What is the name of the artificial intelligence in "I Have No Mouth, and I Must Scream"? ')
if answer.lower() == 'am':
    print('Correct! Oh, delightful comparison!')
    score += 1
else:
    print('Incorrect! *SNAP* You got sent to the cellar!')

# Question 7 (conceptual but one word)
answer = input('What theme connects both TADC and AM’s world: loss of what? ')
if answer.lower() == 'control':
    print('Correct! You’re getting unsettlingly smart!')
    score += 1
else:
    print('Incorrect! You lost control… completely!')

# Question 8
answer = input('What do the characters desperately seek but cannot reach? ')
if answer.lower() == 'exit':
    print('Correct! So close… yet so far!')
    score += 1
else:
    print('Incorrect! The exit vanished again!')

# Question 9
answer = input('What device trapped the humans in the circus? ')
if answer.lower() == 'headset':
    print('Correct! You put it on… didn’t you?')
    score += 1
else:
    print('Incorrect! You put it on anyway… big mistake!')

# Question 10 (final)
answer = input('What does the circus create to distract the characters? ')
if answer.lower() == 'adventures':
    print('Correct! Meaningless fun forever!')
    score += 1
else:
    print('Incorrect! Your adventure ends here!')


#Final score
if score == 10:
    print('You ROCKSTAR! You got all my questions right!')
    print('Until next time at THE AMAIZING DIGITAL CIRCUS!!')
else:
    print('Not bad, but your final score is only ' + str((score / 10) * 100) + '%')
    print('What are you, stupid? Hahahaha!')
