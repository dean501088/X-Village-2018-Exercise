import re  #use +、*、?

user_account = input("pla enter your account:")
user_password = input("plz enter your password:")

pattern_a = r"(?P<user_name>[A-Z][a-zA-Z]+)"
pattern_p = r"(?P<user_password>[a-z0-9]+)"

match1 = re.search(pattern_a,user_account)
match2 = re.search(pattern_p,user_password)

print(match1.groupdict(), match2.groupdict())