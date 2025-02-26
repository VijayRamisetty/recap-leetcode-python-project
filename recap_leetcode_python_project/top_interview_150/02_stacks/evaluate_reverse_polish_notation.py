class Solution(object):
    """
    >>> Solution.evalRPN(Solution,["2","1","+","3","*"])
    9
    >>> Solution.evalRPN(Solution,["4","13","5","/","+"])
    6
    >>> Solution.evalRPN(Solution,["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    22
    """

    def evalRPN(self, tokens: list[str]) -> int:

        stack = []
        for x in tokens:
            if x == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif x == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif x == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif x == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(x))
        return stack[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
