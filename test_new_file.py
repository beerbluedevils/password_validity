


def get_password():
    correct_password = 'B1e2e3r4'
    login_count = 0
    login_limit = 3
    while login_count != login_limit:
        if login_count < login_limit:
            input_password = input('Input password: ')
            login_count += 1
            if input_password == correct_password:
                print('Correct')
                break
            else:
                print('Wrong password!')
        if login_count == login_limit:
            print('You have been blocked!')
        
get_password()