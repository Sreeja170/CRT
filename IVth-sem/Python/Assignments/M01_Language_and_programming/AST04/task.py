def Reverse_String(s: str) -> str:
   result = ""
    for char in s:
        result = char + result
    return result



if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))