import random as rd
import math

num1=int(input("Enter minimum Digit: "));
num2=int(input("Enter maximum Digit: "));
if num2<num1:
    print("Execute Your program Again!");

#Random Number generated
rd=rd.randint(num1,num2);

Chances=round(math.log(num2-num1,2));

count=0;

print("You have Only",Chances,"Chances.");
print("Lets Go!");
while count<Chances:
    count+=1;
    
    Guess=int(input("Enter initial guess : "));
    if Guess=="":
        print("Your Guess Will be number ! Not a string");
        break;
    elif rd==Guess:
        if count==1:

           print("Congratulations! You Have Answer it Correctlty in",count,"try");
           break;
        else:
            print("Congratulations! You Have Answer it Correctlty in",count,"tries");
    elif rd>Guess:
        print("You Guessed To Small");
    elif rd<Guess:
        print("You Guessed To High");
    

    #Chances Over
    if count>=Chances:
        print("The Number is",rd);
        print("NoBody is a loser!\n");
        print("Better Luck Next Time");

