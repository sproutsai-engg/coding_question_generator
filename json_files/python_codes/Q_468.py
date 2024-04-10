##Question ID: 468

def validateIP(queryIP):
    ipv4_parts = queryIP.split('.')
    ipv6_parts = queryIP.split(':')

    if len(ipv4_parts) == 4:
        if is_valid_ipv4(ipv4_parts):
            return "IPv4"
    elif len(ipv6_parts) == 8:
        if is_valid_ipv6(ipv6_parts):
            return "IPv6"

    return "Neither"

def is_valid_ipv4(parts):
    for part in parts:
        if not part or len(part) > 3 or (len(part) > 1 and part[0] == '0'):
            return False

        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False

    return True

def is_valid_ipv6(parts):
    for part in parts:
        if not part or len(part) > 4:
            return False

        for ch in part:
            if not ch.isdigit() and not (ch.lower() >= 'a' and ch.lower() <= 'f'):
                return False

    return True

## Structure
def validateIP(queryIP):
    # Your code here

    pass