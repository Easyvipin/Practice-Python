# 3. Define a function SIMINTEREST( ) in Python to demonstrate the use of :
# ● Positional/Required arguments
# ● Default Arguments
# ● Keyword/Named Arguments
# ● Multiple Arguments

def interest_required(principal,rate,time):
    answer = (principal * rate * time)/100
    print(f"the interst is: {answer}")

def interst_default(principal,rate=4,time=2):
    answer = (principal * rate * time)/100
    print(f"the interst is: {answer}")

def interest_named(principal,rate,time):
    answer = (principal * rate * time)/100
    print(f"the interst is: {answer}")

interest_named(rate=3,time=1,principal=1000)

def interst_multiple(*details):
    principal = details[0]
    rate = details[1]
    time = details[2]
    answer = (principal * rate * time)/100
    print(f"the interst is: {answer}")
        