word = input("Please enter a word to understand which hand you use on keyboard : ")
x = set(word)
left_hand = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v","b"}
right_hand = {"y", "u", "i", "o", "p", "h","j", "k", "l", "n", "m"}
print(bool(x & left_hand) and bool(x & right_hand))