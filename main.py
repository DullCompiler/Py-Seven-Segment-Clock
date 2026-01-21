# Seven Segment Display CLI Demo | Alexander Dennant | DullCompiler

# imports
import time

# basic ascii values
blank = "░"
occupied = "█"

# create segments dictionary
segments = {}

# reset all segments to the blank (off) state
def reset():
    # 2. Use a loop to create keys like 'a1', 'b1', 'a2', etc.
    # This replaces 28 lines of code with 4 lines
    for i in range(1, 5):          # For digits 1, 2, 3, and 4
        for char in "abcdefg":     # For segments a through g
            segments[f"{char}{i}"] = blank

# initialise/ reset segments
reset()

# static ASCII background
def get_display():
    # We use .get() to safely fetch the value from our dictionary
    return f"""
    = = = = = = = = = = = = = = = = = = = = =
    =   {segments['a1']} {segments['a1']}       {segments['a2']} {segments['a2']}       {segments['a3']} {segments['a3']}       {segments['a4']} {segments['a4']}   =
    = {segments['f1']}     {segments['b1']}   {segments['f2']}     {segments['b2']}   {segments['f3']}     {segments['b3']}   {segments['f4']}     {segments['b4']} =
    = {segments['f1']}     {segments['b1']}   {segments['f2']}     {segments['b2']} = {segments['f3']}     {segments['b3']}   {segments['f4']}     {segments['b4']} =
    =   {segments['g1']} {segments['g1']}       {segments['g2']} {segments['g2']}       {segments['g3']} {segments['g3']}       {segments['g4']} {segments['g4']}   =
    = {segments['e1']}     {segments['c1']}   {segments['e2']}     {segments['c2']} = {segments['e3']}     {segments['c3']}   {segments['e4']}     {segments['c4']} =
    = {segments['e1']}     {segments['c1']}   {segments['e2']}     {segments['c2']}   {segments['e3']}     {segments['c3']}   {segments['e4']}     {segments['c4']} =
    =   {segments['d1']} {segments['d1']}       {segments['d2']} {segments['d2']}       {segments['d3']} {segments['d3']}       {segments['d4']} {segments['d4']}   =
    = = = = = = = = = = = = = = = = = = = = =
    """

# print(get_display())

# ASCII numbers
numbers = {
    "0": [blank, blank, blank, blank, blank, blank, blank],
    "1": [blank, occupied, occupied, blank, blank, blank, blank],
    "2": [occupied, occupied, blank, occupied, occupied, blank, occupied],
    "3": [occupied, occupied, occupied, occupied, blank, blank, occupied],
    "4": [blank, occupied, occupied, blank, blank, occupied, occupied],
    "5": [occupied, blank, occupied, occupied, blank, occupied, occupied],
    "6": [occupied, blank, occupied, occupied, occupied, occupied, occupied],
    "7": [occupied, occupied, occupied, blank, blank, occupied, blank],
    "8": [occupied, occupied, occupied, occupied, occupied, occupied, occupied],
    "9": [occupied, occupied, occupied, occupied, blank, occupied, occupied]
}

# ----- user pref input + validation
def mainMenu(valid):
    print("Seven Segment Display CLI Demo | Alexander Dennant | DullCompiler")

    while not valid:
        # minutes input
        minutes = input("Input the minutes (0-59) and press enter: ")
        if minutes == 'q':
            return False
        try:
            if minutes.isdigit() and 0 <= int(minutes) <= 59:
                # seconds input
                seconds = input("Input the seconds (0-59) and press enter: ")
                if seconds == 'q':
                    return False
                if seconds.isdigit() and 0 <= int(seconds) <= 59:
                    valid = True

                    # timeLength calc
                    timeLength=(int(minutes) * 60 + int(seconds))
                    asciiClock(timeLength)

                else:
                    print("Please enter seconds between 0 and 59")
            else:
                print("Please enter minutes between 0 and 59")
        except ValueError:
            print("Please enter valid numbers")
    return valid

# initialise the ASCII clock and populate with the correct ASCII values according to user pref
def asciiClock(timeLength):
    while timeLength >= 0:
        # Format the time
        minutes = str(timeLength // 60).zfill(2)
        seconds = str(timeLength % 60).zfill(2)
        time_string = minutes + seconds

        reset()

        # Draw all 4 digits using one loop
        letters = "abcdefg"
        for i in range(4):
            digit_to_draw = time_string[i]
            pattern = numbers[digit_to_draw]
            pos = i + 1

            for j in range(7):
                char = letters[j]
                segments[f"{char}{pos}"] = pattern[j]

        # Update the screen
        print("\033[H\033[J", end="")
        print(get_display())

        # Countdown logic
        timeLength -= 1
        time.sleep(1)

# main code execution
if __name__ == '__main__':
    mainMenu(valid = False)