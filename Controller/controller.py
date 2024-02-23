import UI.userMenu as ui
import Controller.commands as cmd

def start():
    while True:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            cmd.print_note("all")
        elif user_input == '2':
            cmd.print_note("ID")
        elif user_input == '3':
            cmd.print_note("date")
        elif user_input == '4':
            cmd.print_note("all")
            cmd.change_note()
        elif user_input == '5':
            cmd.add_note()
        elif user_input == '6':
            cmd.print_note("all")
            cmd.delete_notes()
        else:
            print("Программа завершена")
            break
