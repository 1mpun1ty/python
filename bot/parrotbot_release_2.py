import os
import time

def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

clear() #clear the screen
botName=os.name+"_BOT" #set the name of the bot
i="<"+botName+"] "#input marker
o="["+botName+"> "#output marker
var=input("python interpreter: turn on "+botName+"? (yes or no): ")
if var=="yes":
    botOnline="true"
else:
    botOnline="false"
if botOnline=="true":
    print(o+"INITIALIZING parrotbot_devbuild...")
    print(o+"COUNTING BITS...")
    print(o+"NAMING CATS...")
    clear()
    print(o+"Hello there! I'm "+str(botName)+"! would you like to tell me about yourself?")
    var = str(input(i+'agree or disgree: '))
    if var == str('agree'): #check if person agreed
        name = str(input(i+'Enter your name: '))
        if name == name:
            print(o+"Nice to meet you, "+str(name)+".")
        age = str(input(i+'age in years: ')) #add invalid input check
        if float(age) > 0: #check if the person has been alive for at least some time
            alive='yes'
            print(o+str(name)+" is "+str(age)+" years old.")
        else:
            if int(age) <= 0: #check if the person is not alive yet
                print(o+str(name)+" has not been born yet")
                alive='no'
        pulse = float(input(i+'pulse in beats per minute: ')) #add invalid input check
        if float(pulse) < 60:
            if float(pulse) > 0:
                print(o+"WARNING: Low pulse")
            if float(pulse) == 0:
                print(o+"WARNING: No pulse")
        else:
            if float(pulse) > 100:
                print(o+"WARNING: High pulse")
        breathing = str(input(i+'breathing (yes or no): '))
        if pulse>0 or breathing=='yes': #check if person is alive (has pulse or is breathing)
                    alive='yes'
        temperature = int(input(i+'temperature in degrees F: ')) #add invalid input check
        heightIn = int(input(i+'height in inches: ')) #add invalid input check
        weightLbs = int(input(i+'weight in pounds: ')) #add invalid input check
        if pulse>0 or breathing=='yes': #check if person is alive (has pulse or is breathing)
                    alive='yes'
        if temperature<95 or temperature>109: #check if temperature is outside the stable range
                    alive='no'
        if alive=='no': #check if person is not alive. If person is not alive, pronounce them dead and get help!
            print('WARNING: No time to evaluate '+str(name)+'! Get Help!')
            if breathing=='no':
                print(o+str(name)+' is not breathing!')

    else:
        if var == str('disagree'): #check if person disagreed
            print(o+"anonymous mode is currently unsupported. sorry!")
            print(o+'###END OF PROGRAM###')
            time.sleep(1)
            print(o+"Restarting...")
            time.sleep(2)
            os.system('python3.7 parrotbot_devbuild.py')
        else:
            print(o+'please agree or disagree')
            print(o+'###END OF PROGRAM###')
            time.sleep(1)
            print(o+"Restarting...")
            time.sleep(2)
            os.system('python3.7 parrotbot_devbuild.py')
    if alive=='yes': #check if person is alive. If person is alive, say so, then evaluate the person.
        print(o+str(name)+' is alive!')
        heightM=heightIn/39.3701
        weightKg=weightLbs/2.205
        bmi=weightKg/(heightM*heightM)
        print(o+str(name)+"'s bmi is "+str(bmi))
        print(o+str(name)+' is '+str(age)+' years old.')
        print(o+str(name)+"'s temperature is "+str(temperature)+' degrees F.')
        if breathing=='no':
            print(o+str(name)+' is not breathing!')
        print(o+'###END OF PROGRAM###')
        time.sleep(1)
        print(o+"Restarting in one minute...")
        time.sleep(60)
        os.system('python3.7 parrotbot_devbuild.py')
else:
    if var=="no":
        print("python interpreter: bot offline...")
    else:
        print(o+'INVALID INPUT: "'+str(var)+'" (please enter yes or no)')
        print(o+'###END OF PROGRAM###')
        time.sleep(1)
        print(o+"Restarting...")
        time.sleep(2)
        os.system('python3.7 parrotbot_devbuild.py')
