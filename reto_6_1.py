print("----Basic Calculator----")

# We define an Exception subclass, so that we can raise it
# if the user asks for an invalid operator
class InvalidOperationError(Exception):
    def __init__(self, message: str="The operation is not supported, choose one of the valid ones. (+, -, *, /)"):
        super().__init__(message)

def calculator(var_1: int, var_2: int, operation: str) -> int:
    match operation:
        case "+":
            return var_1 + var_2
        case "-":
            return var_1 - var_2
        case "*":
            return var_1 * var_2
        case "/":
            if var_2 == 0:
                raise ZeroDivisionError
            else:
                return var_1 / var_2
        case _:
            raise InvalidOperationError()
        
if __name__ == "__main__":
    # We utilize a while loop to ask repeatedly for the calculator function if an error arises
    while True:
        var_1: int = int(input("Enter first number: "))
        var_2: int = int(input("Enter second number: "))

        operation: str = input("Enter operation (+, -, *, /): ")

        try:
            result = calculator(var_1,var_2,operation)
            print(f"{var_1} {operation} {var_2} = {result}")
            break
        except ZeroDivisionError as error:
            print(f"Error: {error.__class__}, Cannot divide by zero!\n")
            continue
        except InvalidOperationError as error:
            print(f"Error: {error.__class__}, {error}\n")
            continue
