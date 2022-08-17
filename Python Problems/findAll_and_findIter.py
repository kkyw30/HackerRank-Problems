import re 

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

# create list of all outputs
outputs = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), input(), flags=re.I)

print('\n'.join(outputs or ['-1']))    # print all outputs