SIGNS = ['+', '-', '*', '/', '^', '%']
BRACKETS = ['(', ')']

def get_priority(sign):
    priority = int()
    if sign == "(":
        priority = 0
    elif sign == '+' or sign == '-' or sign == ')':
        priority = 1
    elif sign == '*' or sign == '/' or sign == '%':
        priority = 2
    elif sign == '^':
        priority = 3
    return priority


def infix_to_rpn(expression):
    rpn = []
    stack = ["#"]
    for x in expression:
        if x == ' ':
            pass
        elif x in SIGNS:
            if not stack:
                stack.append(x)
            elif x in SIGNS and get_priority(x) < get_priority(stack[-1]):
                while get_priority(stack[-1]) > get_priority(x):
                    rpn.append(stack[-1])
                    stack.pop()
                stack.append(x)
            elif x in SIGNS and get_priority(x) >= get_priority(stack[-1]):
                stack.append(x)
        elif x in BRACKETS:
            if x == '(':
                stack.append(x)
            elif x == ')':
                while stack[-1] is not '(':
                    rpn.append(stack[-1])
                    stack.pop()
                stack.pop()
        else:
            rpn.append(str(x))
    while len(stack) != 1:
        rpn.append(stack[-1])
        stack.pop()
    return rpn


def do_math(first, second, sign):
    if sign == '+':
        return first+second
    elif sign == '-':
        return first-second
    elif sign == '*':
        return first*second
    elif sign == '/':
        return first/second
    elif sign == '^':
        return first**second


def calculate(expression):
    rpn = infix_to_rpn(expression)
    print(rpn)
    arg = list()
    for i in range(len(rpn)):
        if rpn[i] not in SIGNS:
            arg.append(int(rpn[i]))
        elif rpn[i] in SIGNS:
            buffer = do_math(arg[-2], arg[-1], rpn[i])
            arg.pop()
            arg.pop()
            arg.append(buffer)
    answer = arg[0]
    return answer



question = "(a*(b+c)-d*(e+f))/(g+h)"

print(infix_to_rpn(question))

q = "2*(3+5)-(2*7+4)"
print(calculate(q)) #oczekiwane -2
