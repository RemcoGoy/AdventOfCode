import re

file_path = "./input.txt"


class Number:
    def __init__(self, rowStart, rowEnd, value):
        self.rowStart = rowStart
        self.rowEnd = rowEnd
        self.value = value


numbers = []

symbols = []

# Read all input lines from file
with open(file_path, "r") as file:
    lines = file.readlines()

# Parse all numbers and symbols for each input line
for line in lines:
    lineNumbers = []
    for match in re.finditer(r"\d+", line):
        lineNumbers.append(Number(match.start() - 1, match.end(), int(match.group(0))))
    numbers.append(lineNumbers)

    lineSymbols = []
    # for match in re.finditer(r"[@*/&#%+=$-]", line):
    for match in re.finditer(r"[*]", line):
        lineSymbols.append(match.start())
    symbols.append(lineSymbols)

# Count the number of lines in the file
lineCount = len(lines)
sum = 0

# Sum all the valid part numbers (those adjacent to a symbol) for each input line
for i in range(lineCount):
    # Get all the symbols adjacent to the current line

    # Part 1
    # prevLineSymbols = [] if i == 0 else symbols[i - 1]
    # curLineSymbols = symbols[i]
    # nextLineSymbols = [] if i + 1 >= lineCount else symbols[i + 1]
    # for lineNumber in numbers[i]:
    #     if (
    #         any(
    #             index >= lineNumber.rowStart and index <= lineNumber.rowEnd
    #             for index in prevLineSymbols
    #         )
    #         or any(
    #             index >= lineNumber.rowStart and index <= lineNumber.rowEnd
    #             for index in curLineSymbols
    #         )
    #         or any(
    #             index >= lineNumber.rowStart and index <= lineNumber.rowEnd
    #             for index in nextLineSymbols
    #         )
    #     ):
    #         sum += lineNumber.value

    # Part 2
    prevLineNumbers = [] if i == 0 else numbers[i - 1]
    curLineNumbers = numbers[i]
    nextLineNumbers = [] if i + 1 >= lineCount else numbers[i + 1]

    for symbolIndex in symbols[i]:
        prevLineAdjacentNumbers = [
            number
            for number in prevLineNumbers
            if symbolIndex >= number.rowStart and symbolIndex <= number.rowEnd
        ]
        curLineAdjacentNumbers = [
            number
            for number in curLineNumbers
            if symbolIndex >= number.rowStart and symbolIndex <= number.rowEnd
        ]
        nextLineAdjacentNumbers = [
            number
            for number in nextLineNumbers
            if symbolIndex >= number.rowStart and symbolIndex <= number.rowEnd
        ]
        adjacentNumbers = (
            prevLineAdjacentNumbers + curLineAdjacentNumbers + nextLineAdjacentNumbers
        )
        if len(adjacentNumbers) == 2:
            sum += adjacentNumbers[0].value * adjacentNumbers[1].value

print(sum)
