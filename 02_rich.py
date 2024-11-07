from rich.console import Console
from rich.theme import Theme
from rich.traceback import install

install()

theme = Theme({'error': 'bold red', 'success': 'bold green', 'info': 'bold blue'})

console = Console(theme=theme)

def compare_numbers(a,b):
    console.log(log_locals=True)
    if a > b:
        console.print(f"[bold red]{a}[/bold red] is greater than [bold red]{b}[/bold red]")
    elif a < b:
        console.print(f"{a} is less than {b}", style="success")
    else:
        console.print(f"[bold blue]{a}[/bold blue] is equal to [bold blue]{b}[/bold blue]")

compare_numbers(5, 10)
compare_numbers(10, 5)
compare_numbers(5, 5)
compare_numbers(5, "A")



# shrek_info = {
#     "title": "Shrek",
#     "release_year": 2001,
#     "genre": ["Animation", "Adventure", "Comedy"],
#     "director": "Andrew Adamson, Vicky Jenson",
#     "cast": {
#         "Shrek": "Mike Myers",
#         "Donkey": "Eddie Murphy",
#         "Princess Fiona": "Cameron Diaz",
#         "Lord Farquaad": "John Lithgow"
#     },
#     "plot": "An ogre named Shrek finds his swamp overrun by fairy tale creatures who have been banished by the corrupt Lord Farquaad. Shrek makes a deal with Farquaad to rescue Princess Fiona in exchange for the deed to his swamp.",
#     "sequels": [
#         {
#             "title": "Shrek 2",
#             "release_year": 2004,
#             "director": "Andrew Adamson, Kelly Asbury, Conrad Vernon"
#         },
#         {
#             "title": "Shrek the Third",
#             "release_year": 2007,
#             "director": "Chris Miller, Raman Hui"
#         },
#         {
#             "title": "Shrek Forever After",
#             "release_year": 2010,
#             "director": "Mike Mitchell"
#         }
#     ],
#     "awards": [
#         "Academy Award for Best Animated Feature",
#         "BAFTA Award for Best Adapted Screenplay"
#     ],
#     "box_office": {
#         "budget": "$60 million",
#         "gross": "$484.4 million"
#     }
# }
