def is_hex(string):
    # Iterate over string
    for ch in string:

        if (ch < "0" or ch > "9") and (ch < "a" or ch > "f"):

            return False

    # Print true if all
    # characters are valid
    return True


def is_binary(string):
    # set function convert string
    # into set of characters .
    p = set(string)

    # declare set of '0', '1' .
    s = {"0", "1"}

    # check set p is same as set s
    # or set p contains only '0'
    # or set p contains only '1'
    # or not, if any one condition
    # is true then string is accepted
    # otherwise not .
    if s == p or p == {"0"} or p == {"1"}:
        return True
    return False
