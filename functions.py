def math(operation, num1, num2):
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    else:
        return "ERROR, UNIDENTIFIED OPERATOR"
    return answer_simplifier(answer)


def answer_simplifier(answer):
    if answer % 1 == 0:
        return int(answer)
    else:
        return answer
