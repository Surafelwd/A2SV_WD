class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.evaluate(token, operand1, operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[0]
    
    def evaluate(self, operator: str, operand1: int, operand2: int) -> int:
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return int(operand1 / operand2)
