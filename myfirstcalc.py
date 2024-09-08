# Remember to add the correct file extension when creating a new file! For python those are ".py" or ".ipynb" (python notebooks)

firstnumber = input('input number pls: ');

try:
    firstnumber = int(firstnumber)
except ValueError:
    print("That's not a number dumbdumb!")
    exit()

print('you have chosen first number as: ' + str(firstnumber));

secondnumber = input('input second number por favor: ');

try:
    secondnumber = int(secondnumber)
except ValueError:
    print("That's not a number dumbdumb!")
    exit()

print('you have chosen second number as: ' + str(secondnumber));

operand = input('pick your operand (+ , - , * or /) : ');

if operand == '+':
    result = firstnumber + secondnumber
elif operand == '-':
    result = firstnumber - secondnumber
elif operand == '*':
    result = firstnumber * secondnumber
elif operand == '/':
    result = firstnumber / secondnumber
else :
    print('you are big dumbdumnb');
    exit()
print('you have chosen: ' + str(firstnumber) + operand + str(secondnumber));

print('your result is: ' + str(result));
