
def main(n, h, heights):
    total_width = 0
    for height in heights:
        if height > h:
            total_width+=2
        else:
            total_width+=1
    return total_width