from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        # We will first convert it into postfix expression

        # For postfix expression, higher precedence op goes above lower one and if they are same
        # and new operator is left associative, pop old op from stack

        precedence_op = {'+': 1, '-': 1, '*': 2, "/": 2}
        operators = list(precedence_op.keys())
        stack = deque()
        postfix_exp = ""
        i = 0
        while i < len(s):
            if s[i].isspace():
                i += 1
                continue
            if s[i] in operators:
                if len(stack) == 0 or precedence_op[stack[-1]] < precedence_op[s[i]]:
                    stack.append(s[i])
                else:
                    while (len(stack) > 0 and precedence_op[stack[-1]] >= precedence_op[s[i]]):
                        postfix_exp += stack.pop() + "$"
                    stack.append(s[i])
                i += 1
            else:
                num = ""
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                postfix_exp += num + '$'
        
        while(len(stack)):
            postfix_exp += stack.pop() + "$"
        
        print(postfix_exp)
        
        # We will evaluate postfix expression to find the answer

        num_stack = deque()
        i = 0
        while i < len(postfix_exp):
            ele = ""
            while len(postfix_exp) > 0 and postfix_exp[i] != '$':
                ele += postfix_exp[i]
                i += 1
            if ele.isdigit():
                num_stack.append(int(ele))
            else:
                if len(num_stack) < 2:
                    print("Invalid expression. Stack length is less than 2")
                    return
                operand1, operand2 = num_stack.pop(), num_stack.pop()

                if ele == '+':
                    num_stack.append(operand1 + operand2)
                elif ele == '-':
                    num_stack.append(operand2 - operand1)
                elif ele == '*':
                    num_stack.append(operand1 * operand2)
                else:
                    num_stack.append(int(operand2 // operand1))
            i += 1

        return num_stack[-1]       