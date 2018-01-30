def do_the_mail():

    donors = {'this_person': [100], 'that_person': [100, 200]}

    response = input('send a thank you or create a report? (input 1 or 2)')
    if(response == '1'):
        name = input('name?')
        if name not in donors:
            donors[name] = 0
        amount = int(input('amount?'))
        donors[name].append(amount)
        print('Thank you %s for your generous donation of $%d!' % (name, amount))
        print(donors)
        try:
            val = int(amount)
        except ValueError:
            print('That’s not an int!')
    elif(response == '2'):
        name = input('name?')
        if name not in donors:
            print('User not available')
        else:
            totals = 0
            for i in range (len(donors[name])):
                totals += donors[name][i]
            number_of_donations = len(donors[name])
            average_donation = int(totals / number_of_donations)
            print('total contributed: %s' % totals)
            print('number of donations: %s' % number_of_donations)
            print('average donation: %s' % average_donation)
    else:
        print('please input "1" to send a thank you or "2" to create a report')
        print(do_the_mail())

print(do_the_mail())


    # Else:
    #     totals = ** sum all donations from list of donations **
    #     number_of_donation = ** len(list from dictionary) **
    #     average_donation = ** totals/number_of_donations **
    #     for donors, amount in sorted(docs_info.items()):
    #         print(key, amount)
    #     print totals, number_of_donation, average_donation



	

	

