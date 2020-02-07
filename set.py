all_emails = list(open('./emails2.txt', 'r').read().split(' '))
print('read')
with open('./emails3.txt', 'w') as output:
    print('opened')
    emails = list(map(lambda x: x.split(',')[0]+'\n', all_emails))
    print('mapped')
    output.writelines(emails)
    output.close()