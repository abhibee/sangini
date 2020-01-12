place = input('where do you live: ')
leagaldrivingage = float(
    input('what is the leagal driving in ' + place + '?:'))
age = float(input('what is your age:'))
if age >= leagaldrivingage:
    print('you are old enough to drive!')
if age < leagaldrivingage:
    print('sorry, you have to wait for ', leagaldrivingage - age, ' years.')
