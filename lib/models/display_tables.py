from prettytable import PrettyTable
from termcolor import colored


table = PrettyTable()
table.max_width = 50


# display only crucial needed user information
def artist_table(artists):
    headers = ["ID", "Name", "Email", "Genre", "Availability"]
    table.field_names = [colored(header, "blue") for header in headers]

    for artist in artists:
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


def venue_table(venues):
    headers = ("ID", "Name", "Email", "City", "Capacity")
    table.field_names = [colored(header, "blue") for header in headers]

    for venue in venues:
        table.add_row(
            [
                colored(venue.id, "green"),
                colored(venue.venue_name, "red"),
                colored(venue.venue_email, "cyan"),
                colored(venue.venue_city, "magenta"),
                colored(venue.capacity, "yellow"),
            ]
        )

    print(table)


def booking_table(bookings):
    headers = ("ID", "Artist ID", "Venue ID", "Artist", "Venue", "Booking")
    table.field_names = [colored(header, "blue") for header in headers]

    for booking in bookings:
        table.add_row(
            [
                colored(booking.id, "green"),
                colored(booking.artist.id, "green"),
                colored(booking.venue_id, "green"),
                colored(booking.artist_name, "red"),
                colored(booking.venue_name, "magenta"),
                colored(booking.booking_date, "yellow"),
            ]
        )

    print(table)
