# I, Shing Kit Wan, student number 000826521,
# certify that all code submitted is my own work;
# that I have not copied it from any other source.
# I also certify that I have not allowed my work to be copied by others.

import random



def rollDie(faces):
    # module to roll a single die with a variable number of faces
    # ASSUME faces is a valid positive integer, greater than 1
    # print("***** Rolling first time in this round *******")
    roll=[]
    for x in range(0,int(selected_dice_amount)):
        x=random.randint(1, int(faces))  # generate random number of dice point
        roll.append(x)#random dice points are imported as list namely "roll"
    return roll

def validateInt(min,max,prompt):
    # prompt is the input on dice face and dice no
    # min and max are the restrictions on setting these elements
    prompt=str(prompt)
    if prompt.strip().isdigit()==True:#make sure it is integer without space
        if min<=int(prompt)<=max:
            # we return the integer if it falls within ranges
            return int(prompt)#correct value
        if int(prompt)==0:
            inp=input("I am sorry, that isnt a valid integer,please try again")
            return validateInt(min,max,inp)#verify new input by return to beginning
        else:
            inp=input("I am sorry, that isnt a valid integer,please try again")
            return validateInt(min,max,inp)#verify new input by return to beginning
    else:
        inp=input("I am sorry, that isnt a valid integer,please try again")
        return validateInt(min,max,inp)#verify new input by return to beginning


def validateStr(prompt, listOfChoices):
    # test if input=['yes' , 'no'] or [y/n]
    # assume prompt is a String, listOfChoices is a list of choices
    input_data=str(prompt).lower().strip(" ")
    #make sure it has no space
    if input_data==listOfChoices[0]:# input=yes/y?
        return True
    if input_data==listOfChoices[1]:# input=no/n?
        return False
    if not input_data==listOfChoices[1] and not input_data==listOfChoices[0]:
        inp=input("i'm sorry,the choices are" + str(listOfChoices) + ". Please pick of them")
        return validateStr(inp,listOfChoices)


# ASSUME inList is a list of numbers and the length of inList is > 0
def average(inList):
    sum_str=sum(inList)
    avg=0
    for x in inList:
        avg=avg + x
    avg=round(avg/len(inList))
    return ["These die sum to", sum_str, "and have an average rounded value of", avg]


def calculatePercentage(sides, dice, diceRolls):
    # side is side of dice, dice is # of dice,
    # diceRolls is list of current dice roll
    # ASSUME sides*dice != 0, sides, dice are numbers
    # ASSUME diceRolls is a list of numbers
    max_score=int(sides)*int(dice)
    percent=sum(diceRolls)/max_score
    return percent


def isPrime(n):#test if the integer a prime no?
    for x in range(2,round(n/2)):
        if n%x==0:
            return False
    return True


def pattern1(sides, dice):  # side is # of sides of dice, #dice is the list of roll result
    if int(sides)>=4:  # condition # of side>=4
        if len(set(dice))==1:  # patten: set function wipe duplicates, so length of same value=1
            print("Matched pattern 1,all dice faces are the same")
            return True
        else:
            print("Pattern 1 not matched in your roll", dice, "dices are different")
            return False
    else:
        print("Cannot match pattern 1 as there are less than 4 dices")
        return False


def pattern2(dice, count, sides):
    # side is # of sides of dice,
    # count is the # of dices, # #dice is the list of roll result,
    if int(sides)*int(count)>20:  # condition: max score>=20
        if isPrime(sum(dice))==True:  # pattern: sum of all dice is prime no.
            print("Matched pattern 2-> the sum is prime")
            return True
        else:
            print("Didnt match pattern 2 because",sum(dice),"is not prime number")
            return False
    else:
        print("Cannot match pattern 2 as the max score is less than 20")
        return False


def pattern3(dice):#dice is the list of roll result
    if len(dice)>=5:  # condition: # of dices>=5
        counter=0
        avg=[sum(dice),round(sum(dice)/len(dice))][1]
        for x in dice:
            if x>avg:
                counter=counter + 1
        if counter*2>=len(dice):  # pattern: 1/2 the dice>= average
            print("Matched pattern 3, 1/2 of all dices are > avg in the same roll")
            return True
        else:
            print("Didnt match pattern 3 as there are less than 1/2 dices > avg in the same roll")
            return False
    else:
        print("Cannot match pattern 3 as the dices are less than 5")
        return False


def pattern4(dice, sides):
    # side is # of sides of dice, #dice is the list of roll result
    if len(dice)>4:  # condition:#of dice>=4
        if int(sides)>len(dice):  # #of sides># of dice
            if len(set(dice))==len(dice):  # all face different value
                print("Matched pattern 4, all dice faces are unique")
                return True
            else:
                print("Didnt match pattern 4 because not all are unique")
                return True
        else:
            print("Didnt match pattern 4 because number of dice faces > number of dice")
            return False
    else:
        print("Cannot match pattern 4 as there are less than 4 dices")
        return False


def bonusFactor(sides, count, dice):
    # side is # of sides of dice,
    # count is the # of dices, # #dice is the list of roll result,
    # ASSUME dice is a list of numbers
    # ASSUME sides, count are integers
    bonus_factor=0

    p1=pattern1(sides, dice)
    p2=pattern2(dice, count, sides)
    p3=pattern3(dice)
    p4=pattern4(dice, sides)

    if p1==True:
        bonus_factor = bonus_factor + 10
    if p2==True:
        bonus_factor = bonus_factor + 15
    if p3==True:
        bonus_factor = bonus_factor + 5
    if p4==True:
        bonus_factor = bonus_factor + 8
    if p1==False and \
            p2==False and \
            p3==False and \
            p4==False:#if pattern 1,2,3,4not match, match pattern5
        print("since none of the patterns were matched, pattern 5 is matched")
        bonus_factor = bonus_factor + 1
    print("You got a bonus factor of", bonus_factor)
    return bonus_factor


def score(maxSides, totalDice, diceRolled):
    # ASSUME maxSides and totalDice are integers > 0
    # ASSUME diceRolled is a list of integers
    percent=calculatePercentage(maxSides,totalDice,diceRolled)
    # calculate % of sum of current point/sum of max point on dice
    res=round((percent*bonusFactor(maxSides,totalDice,diceRolled)),0)
    # above % X bonus factor
    current_dice_sum=sum(diceRolled)
    # sum of current point
    final=current_dice_sum+res+student_number%2020
    # final point =sum of current point+bonus+bonus from student no modulus
    print("The dices are worth",final,"points")
    return final


print("COMP 10001 - W2020 FInal Project by Sample Solution, name: Shing Kit Wan, Student number 000826521")
print("Welcome to my dice game, good luck!")
student_number=int("000826521")
min_dice_sides=2
max_dice_sides=20
min_amount_dices=3
max_amount_dices=6
should_continue_playing=True
current_user_roll=list()# store the result of this round rolled dice
scores_today=[]#store the score of each rounds
turn_idx=0  # flag that indicate the no of turn u played
yes_or_no=['yes', 'no']  # indicator that use in function "validateStr"
y_n=['y', 'n']# indicator that use in function "validateStr"

selected_dice_amount=input("Enter number of dices[3,6]:")
selected_dice_amount=validateInt(min_amount_dices,max_amount_dices,selected_dice_amount)
# validate dice amount
if type(validateInt(min_amount_dices,max_amount_dices,selected_dice_amount))==int:

    selected_dice_sides=input("Enter number of dice faces[2,20]:")
    selected_dice_sides=validateInt(min_dice_sides, max_dice_sides, selected_dice_sides)
    #validate dice face
    if type(validateInt(min_dice_sides,max_dice_sides,selected_dice_sides))==int:

        while should_continue_playing==True:

            current_user_roll=rollDie(selected_dice_sides)  # using rollDie function to generate random roll points
            print("Rolled",current_user_roll)

            print(average(current_user_roll))
            current_user_total_score=score(selected_dice_sides,selected_dice_amount,current_user_roll)
            #report the score of current roll result, see if user happy with it
            ask_reroll=input("Do you want to reroll any dice?'yes'or'no'")


            if validateStr(ask_reroll,yes_or_no)==True:
                indexes=[]
                for x in range(0,len(current_user_roll)):#range(0,no of dice)

                    q=input("Reroll dice"+str(x + 1)+"?(was"+str(current_user_roll[x])+")[y/n]")
                    if validateStr(q, y_n)==True:
                        indexes.append(x)
                        #store which dice need to re-roll in a list namely indexes
                    else:
                        continue

                ask_sure=input("Are you sure? ['yes','no']")
                if validateStr(ask_sure,yes_or_no)==True:
                    print("new roll: ")

                    for idx in indexes:
                        current_user_roll[idx]=random.randint(1,int(selected_dice_sides))
                    # designated dice order stored in list called "indexes"
                    # will be indicated as order to re-roll in case user sure

                    print(current_user_roll)
                elif validateStr(ask_sure, yes_or_no)==False:
                    print("Going with the old roll: ")
                    print(current_user_roll)

            print(average(current_user_roll))
            current_user_total_score=score(selected_dice_sides, selected_dice_amount, current_user_roll)
            #calculate re-rolled score
            print("that was your ",turn_idx + 1," turn, lets go again")

            turn_idx=turn_idx+1

            if turn_idx==1:
                should_play_again='yes'
            else:
                should_play_again=input("Do you want to play another round? [yes, no]")
            #in first turn, it auto goes to next turn, from 2nd turn on, ask user
            #if he wants next turn

            scores_today.append(current_user_total_score)
            #scores of the turn store in this list

            if validateStr(should_play_again,yes_or_no):
                continue
            else:
                should_continue_playing=False

                print("You played ",turn_idx," turns today, with an average total score ",average(scores_today)[3])
