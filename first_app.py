age = input ("Are you a cigarette addict older than 75 years old? (Yes or No) = "'\t')
chronic = input ("Do you have a severe chronic disease?  (Yes or No) = " '\t')
immune = input("Is your immune system too weak? (Yes or No)= " '\t')

risk = ((bool(age) and bool(chronic) and bool(age)) or (bool(age) or bool(immune)) and (bool(chronic) or bool(immune)))
print(risk)