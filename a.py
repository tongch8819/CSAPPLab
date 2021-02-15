def decimalToBinary(s: str) -> str:
    try:
        num = eval(s)
        if num < 0:
            return None
        elif num == 0:
            return '0'
    except ValueError:
        return None
    rst = [] 
    while num != 0:
        num, b = divmod(num, 2)
        rst.insert(0, str(b))
    return ''.join(rst)

def testDecimalToBinary():
    cases = (
        ['1', '1'],
        ['0', '0'],
        ['-3', None],
        ['15', '1111'],
    )
    for case, ans in cases:
        assert decimalToBinary(case) == ans, "Case failed: {} {}".format(case, ans)
    print("Test Passed: decimalToBinary()")



def hexToBinary(s: str) -> str:
    if s[:2] not in ['0x', '0X']:
        return None
    mapping = dict()
    for i in range(10):
        key = str(i)
        mapping[key] = decimalToBinary(key).rjust(4, '0')
    for i in range(6):
        key = chr(i + ord('a'))
        mapping[key] = decimalToBinary(str(i+10)).rjust(4, '0')

    rst = []
    for c in list(s[2:]):
        rst.append(mapping[c.lower()])  # ensure lower case
    return ''.join(rst)

def testHexToBinary():
    cases = (
        ('0xd4', '11010100'),
        ('0x64', '01100100'),
        ('0x72', '01110010'),
        ('0x44', '01000100'),
    )
    for case, ans in cases:
        assert hexToBinary(case) == ans, "Case failed: {} {}".format(case, ans)
    print("Test Passed: hexToBinary()")



def main():
    testHexToBinary()

if __name__ == "__main__":
    main()