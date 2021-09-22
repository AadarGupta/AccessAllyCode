def arith_seq(string):
    change = int(string[1]) - int(string[0])
    for i in range(len(string) - 1):
        if not (change == (int(string[i + 1]) - int(string[i]))):
             return 0
    return 1

userInput = int(input())
userHours = int(userInput / 60)
userMins = (userInput % 60)

userHoursStr = str(userHours)
if(userMins < 10):
    userMinsStr = str( "{:02d}".format(userMins) )
else:
    userMinsStr = str(userMins)
    
checkArithmetic = int( userHoursStr + userMinsStr )
numArithmetic = 0

for i in range(userInput + 1):
    if (i < 60):
        if ( arith_seq(str(1200 + (i % 60))) ):
            numArithmetic += 1
    else:
        if ( arith_seq(str((i % 60) + (100 * int(i / 60)) ))):
            numArithmetic += 1
print(numArithmetic)
