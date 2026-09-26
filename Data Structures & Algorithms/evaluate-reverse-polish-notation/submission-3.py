class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []

        for t in tokens:
            match t:
                case "+":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a + b)               
                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "*":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a * b)
                case "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                case _:
                    stack.append(int(t))
        
        return stack[0]