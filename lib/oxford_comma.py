def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    if len (items) == 2:
        return f"{items[0]} and {items[1]}"
    str = ', '.join(items[:-1]) + f", and {items[-1]}"
    # left += f", and {items[-1]}"
    return str

print (oxford_comma(["fiddleheads", "okra", "kohlrabi"]))