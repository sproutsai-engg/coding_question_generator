##Question ID: 537

def complexNumberMultiply(num1: str, num2: str) -> str:
    real1, imag1 = map(int, num1[:-1].split('+'))
    real2, imag2 = map(int, num2[:-1].split('+'))

    real = real1 * real2 - imag1 * imag2
    imag = real1 * imag2 + real2 * imag1

    return f"{real}+{imag}i"

## Structure
def complexNumberMultiply(num1: str, num2: str) -> str:
    # Your code here

    pass