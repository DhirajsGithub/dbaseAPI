def main(number, base, convertTo):
    numLi = []
    decimalLi = []
    isValid = True
    for i in range(len(number)):
        if (base <= 10 and ord(number[i]) > 49 + base - 2):
            isValid = False
            break
        if (base > 10 and ord(number[i]) > 55 + base - 1):
            isValid = False
            break
        if number[i] == ".":
            break
        else:
            numLi.append(number[i])
    for j in range(len(numLi)+1, len(number)):
        decimalLi.append(number[j])

    def convertToDecimal():
        ans = 0
        p = 0
        k = 0
        for i in numLi[::-1]:
            k += 1      # from this k decimal number will appear
            if i == ".":
                break
            element = i
            if element.isnumeric():
                element = int(element)
            else:
                element = int(ord(element)-55)
            ans += (base**p)*element
            p += 1
        p2 = 1
        ans2 = 0
        for i in decimalLi:
            if i.isnumeric():
                i = int(i)
            else:
                i = int(ord(i)-55)
            ans2 += i*(1/(base**p2))
            p2 += 1
        return ans+ans2

    def decimalToConvertTo():

        # converting integer part of decimal number to the given convertTo base
        num = int(convertToDecimal())

        ans = ""
        li = []
        while num > 0:
            rem = num % convertTo
            li.append(rem)
            num = num//convertTo
        li = li[::-1]
        for i in li:
            # checking if remainder is >=10 then convert it into A, B, C, ...
            if int(i) >= 10:
                i = chr(int(i) + 55)
            ans += str(i)

        # converts decimal part of decimal number to givent convertTo base
        intLi = []
        deciLi = []
        num2 = str(convertToDecimal())
        for i in range(len(num2)):
            if num2[i] == ".":
                break
            intLi.append(num2[i])
        for j in range(len(intLi)+1, len(num2)):
            deciLi.append(num2[j])
        # let say precision is upto 10 digits
        temp = ''
        if len(deciLi) != 0:
            deciNum = ''.join(deciLi)
            deciNum = int(deciNum)
            deciNum = deciNum/(10**len(deciLi))
            for i in range(10):      # precision
                if (deciNum == 0):
                    break
                temp2 = int(deciNum*convertTo)
                if temp2 >= 10:
                    temp2 = chr(temp2 + 55)
                temp += str(temp2)
                x, y = str(deciNum*convertTo).split(".")
                deciNum = int(y)/(10**len(y))

        if len(deciLi) == 0:
            return ans
        return ans+"."+temp
    if isValid:
        return decimalToConvertTo()
    return "Out of bound Base ):"
