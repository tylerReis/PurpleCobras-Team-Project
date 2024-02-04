# required imports for rich 
from rich import print 
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt

# create a console class to allow printing and exporting
console = Console()


# create main menu interface
def main_menu() :
    menu = ("1. Contact Manager","2. Task Manager","3. Search the Web","4. Exit")
    console.rule(":diamond_shape_with_a_dot_inside: [b]Main Menu[/b] :diamond_shape_with_a_dot_inside:", style="blue")
    table = Table(show_header=False, show_lines=False, style="purple4")
    table.add_column(min_width=20, justify="center")
    table.add_column(min_width=20, justify="center")
    table.add_row(Panel(menu[0], expand=True, style="green"),Panel(menu[1], expand=True, style="green"))
    table.add_row(Panel(menu[2], expand=True, style="green"),Panel(menu[3], expand=True, style="green"))
    console.print(table)
    console.rule("[b]End Main Menu[/b]", style="blue")
    main_menu_selection = console.input(":waving_hand: Hello, please enter your selection : [bold red][i]1, 2, 3, 4[/i]? :point_right: ")
main_menu()

# create contact manager menu interface
def contact_manager() :
    contacts_menu = ("1. :blue_book: View All Contacts", "2. :pencil: Add New Contact", "3. :cross_mark: Delete Contacts", "4. :fast_reverse_button: Back to Main Menu")
    console.rule(":white_medium_star: [b]Contact Manager Menu[/b] :white_medium_star:", style="bold blue")
    table = Table(show_header=False, show_lines=False, style="bright_magenta")
    table.add_column(min_width=20, justify="center")
    table.add_column(min_width=20, justify="center")
    table.add_row(Panel(contacts_menu[0], expand=True, style="bold sky_blue1"),Panel(contacts_menu[1], expand=True, style="bold sky_blue1"))
    table.add_row(Panel(contacts_menu[2], expand=True, style="bold sky_blue1"),Panel(contacts_menu[3], expand=True, style="bold sky_blue1"))
    console.print(table)
    console.rule("[b]End Menu[/b]", style="bold blue")
    contact_manager_selection = IntPrompt.ask("[bold][i]What would you like to do?[/i]", choices=["1", "2", "3", "4"], default="4")
contact_manager()

# create task manager menu interface
def task_manager() :
    task_menu = ("1. :pencil: Create New Task", "2. :file_folder: View Current Task List", "3. :white_check_mark: Mark a Task as Complete", "4. :fast_reverse_button: Back to Main Menu")
    console.rule("[b]Task Manager Menu[/b] :lower_left_fountain_pen:", style="bold blue")
    table = Table(show_header=False, show_lines=False, style="pale_turquoise1")
    table.add_column(min_width=20, justify="center")
    table.add_column(min_width=20, justify="center")
    table.add_row(Panel(task_menu[0], expand=True, style="medium_violet_red"),Panel(task_menu[1], expand=True, style="medium_violet_red"))
    table.add_row(Panel(task_menu[2], expand=True, style="medium_violet_red"),Panel(task_menu[3], expand=True, style="medium_violet_red"))
    console.print(table)
    console.rule("[b]End Menu[/b]", style="bold blue")
    task_manager_selection = IntPrompt.ask("[bold][i]What would you like to do?[/i]", choices=["1", "2", "3", "4"], default="4")
task_manager()

# create search the internet menu interface
def internet_search() :
    console.rule("[b]Search the Web[/b] :computer:", style="bold blue")
    console.print(":link: Click Here To Search the Internet", style="link https://google.com bold blue frame")
    console.rule("[b]End Menu[/b]", style="bold blue")
    back_to_main = IntPrompt.ask("[bold][i]:fast_reverse_button: To Return Back to Main Menu Enter[/i]", choices=["1"])
internet_search()