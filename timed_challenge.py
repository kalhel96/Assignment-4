# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
#Group 4: Last-In, First-Out Logic
#13. Balanced Symbols
#Check if the brackets in a string are balanced.
#Input: "{[()]}"
#Output: True
#Input: "{[(])}"
#Output: False


#The idea before my code 
#- we get a string and return True or False.
#- Every openning racket must be closed by the same type and the LAST one opened must be the First one closed.
# - "Last in, first out", which is stack.

# Test cases
# "{[()]}"  -> True   (normal, balanced)
# "{[(])}"  -> False  (normal, closed in the wrong order)
# ""        -> True   (edge: empty string, nothing to match)
# "((("     -> False  (edge: opened but never closed)
# ")"       -> False  (edge: closed but never opened)
# "a(b)c"   -> True   (edge: letters mixed in are ignored)

def check_balance(text):
    stack= [] # empty pile of plates
    pairs = {")": "(", "]": "[", "}": "{"}    # each closer and its opener

    for char in text:
        if char in "([{":                     # opening bracket?
            stack.append(char)                # put it on top of the pile
        elif char in ")]}":                   # closing bracket?
            if len(stack) == 0:               # nothing to match it with
                return False
            top = stack.pop()                 # take the top plate off
            if top != pairs[char]:            # wrong type of bracket
                return False
 
    return len(stack) == 0     # pile must be empty at the end

# Test the function
print(check_balance("{[()]}"))  # True
print(check_balance("{[(])}"))   # False
print(check_balance(""))  # True
print(check_balance("((( ")) # False
print(check_balance(")"))        # False
print(check_balance("a(b)c"))    # True

# Explain my approach
# I used a stack because brackets follow "last in, first out":
# the last bracket I open has to be the first one I close.
# Every time I see an opening bracket, I push it on the stack.
# Every time I see a closing bracket, I pop the top one and check
# that it matches. If it doesn't match, or the stack is empty when
# I need something, the string is not balanced. At the end, the
# stack must be empty, or some brackets were never closed.
# I wrote test cases first, including edge cases like an empty
# string and a closing bracket with nothing to match.