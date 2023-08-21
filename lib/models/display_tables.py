from prettytable import PrettyTable
from termcolor import colored


# display only crucial needed user information
def artist_table(artist_results):
    table = PrettyTable()
    headers = ["ID", "Name", "Email", "Genre", "Availability"]
    table.field_names = [colored(header, "blue") for header in headers]

    table.max_width = 50

    for artist in artist_results:
        table.add_row(
            [
                colored(artist.id, "green"),
                colored(artist.artist_name, "red"),
                colored(artist.email, "cyan"),
                colored(artist.genre, "magenta"),
                colored(artist.availability, "yellow"),
            ]
        )

    print(table)
