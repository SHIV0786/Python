# unpacking elements from iterable of arbitary length
# Python "star expression" can be used to address this problem

# find average of semester between 2nd to 7th



def drop_first_and_last(grades):
    first, *middle, last = grades
    return round(sum(middle)/len(middle),2)


grades = [23, 45, 23, 12, 53, 5, 32, 53]
print(drop_first_and_last(grades))


record = ('Dave','dave@example.com','12345-67892','12223-78342')
name, email, *phone_number = record
print("Name: ",name,"Email: ",email,"Phone_Numbers: ",phone_number)


*trailing, current = [1,23,3,42,42,52,53]
print(trailing,"\n",current)

line = 'nobody:*-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print("Uname: ",uname,"\n","HomeDir: ",homedir,"\n","sh: ",sh)
