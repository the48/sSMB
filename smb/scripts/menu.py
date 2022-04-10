from simple_term_menu import TerminalMenu

menu = ['[1] Send file', '[2] Get file', '[3] Quit']

exit = True


while exit:
    choice = menu[TerminalMenu(menu, title = 'Secure-SMB').show()]

    if choice == '[1] Send file':
        print('aigth')

    elif choice == '[2] Get file':
        print('12ew')

    elif choice == '[3] Quit':
        exit = False
