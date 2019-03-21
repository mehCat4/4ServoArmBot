yes_no = ""
motor_val = ""

b ={
    'a' : 122,
    'b' : 123,
    'l' : "left",
    'r' : "right"
    }

# get user input
while yes_no != "n":
    inp = raw_input('input a character : ')
    if inp == "n":
        break
    print'The result is: '
    print(b.get(inp, -1))
    
print 'Exiting loop'