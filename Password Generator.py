import random,string
letters=string.ascii_letters
digits=string.digits
special_chars="@!$#&_"
print("".join(random.choices(letters+digits+special_chars,k=10)))