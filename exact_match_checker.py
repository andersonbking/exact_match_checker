print("exact_match_checker by Anderson")
print("(to paste = ctrl + shift + v)")
print()

# get words to check for identicality
first = input("Copy and paste your first file: ")
print()
second = input("Copy and paste you second file: ")
print()
print()

# check if they are exactly the same
if first == second:
    print("They are identical.")
else:
    print("They are different.")
