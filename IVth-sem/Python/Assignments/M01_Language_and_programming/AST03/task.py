def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    # Round to 2 decimal places
    avg = round(avg, 2)

    # Format average properly (remove unnecessary trailing zero)
    if avg == int(avg):
        avg_str = str(float(int(avg)))
    else:
        avg_str = str(avg)

    if avg >= 40:
        status = "Pass"
    else:
        status = "fail"

    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))