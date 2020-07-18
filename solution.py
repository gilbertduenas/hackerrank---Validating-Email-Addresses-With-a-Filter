# All I did for this was add lines 2 and 6-9. Done!
import re

def fun(s):
    # return True if s is a valid email, else return False
    if re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',s):
        return True
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
