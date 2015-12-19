nums = [" _     _  _     _  _  _  _  _ ",
        "| |  | _| _||_||_ |_   ||_||_|",
        "|_|  ||_  _|  | _||_|  ||_| _|",
        "                              "]
        
def digitise(numbers):
    if len(numbers) != 4:
        raise ValueError("Not enough rows.")
    if any(len(row) != len(numbers[0]) for row in numbers):
        raise ValueError("Not all rows are of same length.")
    n = len(numbers[0])
    digits = []
    for i in range(0, n, 3):
        digits.append([numbers[j][i:i+3] for j in range(4)])
    return digits

digits = digitise(nums)
    
def number(input):
    numbers = digitise(input)
    result = ""
    for digit in numbers:
        if digit in digits:
            result += str(digits.index(digit))
        else:
            result += "?"
    return result

def grid(numbers):
    if any(not num.isdigit() for num in numbers):
        raise ValueError("Invalid character (not a number)")
    result = [""] * 4
    for num in numbers:
        for i in range(4):
            result[i] += digits[int(num)][i]
    return result