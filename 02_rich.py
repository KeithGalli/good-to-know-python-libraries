from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

install()

custom_theme = Theme({'error': 'bold red', 'warning': 'bold yellow'})

console = Console(theme=custom_theme)

def compare_numbers(a, b):
    console.log(log_locals=True)
    if a > b:
        console.print(f"{a} is greater than {b}", style="bold green")
    elif a < b:
        console.print(f"{a} is less than {b}", style="warning")
    else:
        console.print(f"{a} is equal to {b}")

compare_numbers(5, 10)
compare_numbers(10, 5)
compare_numbers(5, 5)

compare_numbers(5, "Keith")