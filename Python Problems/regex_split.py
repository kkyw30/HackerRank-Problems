# goal to split (and print on a new line) a number by every occurrence of ',' or '.'

import re 

regex_pattern = r"[, .]"      # define set of characters to look for
print("\n".join(re.split(regex_pattern, input())))
