def ifSignFalse():

    print('')
    print('')
    print('That entry does not exist.')
    print('')
    print('')
    flag = False
    while flag == False:
        print('Choose an option from the following menu:')
        print('________________________________________')
        print('')
        print('           0: Try again')
        print('           1: Main menu')
        print('________________________________________')
        print('')
        ans = input('')
        if ans == '0':                            
            ans = True
            flag = True
        elif ans == '1':
            ans = False
            flag = True
        else:
            print('That is not a valid response.')

    return ans
