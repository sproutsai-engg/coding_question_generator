##Question ID: 858

def mask_information(s: str) -> str:
    if '@' in s:
        s = s.lower()
        return s[0] + "*****" + s[s.index('@') - 1:]
    else:
        digits = "".join(filter(str.isdigit, s))
        if len(digits) == 10:
            return "***-***-" + digits[-4:]
        prefix = "*"* (len(digits) - 10) + "-"
        return "+" + prefix + "***-***-" + digits[-4:]

## Structure
def mask_information(s: str) -> str:
    # Your code here

    pass