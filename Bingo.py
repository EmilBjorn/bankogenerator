from PIL import Image, ImageDraw, ImageFont
from random import randrange, choice


def BingoNum():
    Numbers = []
    # print(Numbers)

    tens = {}

    for i in range(9):
        tens[i] = 1
        n = (i)*10+randrange(10)
        if n == 0:
            n = 90
        Numbers.append(n)

    while len(Numbers) < 15:

        fullNumber = randrange(1, 91)
        firstDigit = fullNumber//10

        if firstDigit == 9:
            firstDigit = 8
        if tens[firstDigit] < 3:
            tens[firstDigit] += 1
            if fullNumber not in Numbers:
                Numbers.append(fullNumber)

    Numbers.sort()
    return(Numbers)
    # print("Numbers:")
    # print(Numbers)
    # for i in tens:
    #     print(tens[i])


numbers = BingoNum()

# dict af alle 15 tal på pladen med et index som holder styr på hvilken række på pladen de placeres i.
NumberDict = {i: 0 for i in numbers}
RowSum = {i: 0 for i in range(3)}
tens = {i: 0 for i in range(9)}

for i in numbers:
    if i == 90:
        tens[8] += 1
    else:
        tens[i//10] += 1


# looper gennem 0-8, opdaterer NumberDict med placering af tal.
for i in range(9):

    GetOutPass = False
    while GetOutPass == False:
        choices = list(range(3))  # [0,1,2]
        j = 3
        while j > tens[i]:
            choices.pop(randrange(len(choices)))
            j -= 1

        # choices indeholder nu en kandidat til de felter, som skal besættes. fx [0,2]. De vil blive afvist, hvis det fører til mere end 5 i en række
        alert = False
        RowSumCurrent = RowSum
        for k in choices:
            RowSumCurrent[k] += 1
            if RowSumCurrent[k] > 4 and i != 8:
                alert = True
        if alert == False:
            RowSum = RowSumCurrent
            GetOutPass = True

        # Choices indeholder nu de rows i 'i' kolonnen, som skal besættes af et tal. fx [0,2]

    # udvælg tal i numbers som har 'i' som årti.
    subNumbers = []  # fx [11,16] i 10'erne
    for k in range(len(numbers)):
        if numbers[k]//10 == i:
            subNumbers.append(numbers[k])

    subIndex = 0
    for k in subNumbers:
        NumberDict[k] = choices[subIndex]
        subIndex += 1


# print(BingoNum())
print(NumberDict)

key = 477

im = Image.new("RGB", (1000, 500), "#FFFF00")
test = Image.open(
    'C:/Users/Emil/Documents/Python/Bingopladegenerator/Bingoplade.png')

font = ImageFont.truetype("Jost-700-BoldItalic.otf", 320)
draw = ImageDraw.Draw(test)
draw.text((420, 1150), "88", font=font, fill=(0, 0, 0, 255))

test.show()
