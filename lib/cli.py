#!/usr/bin/env python
import click
import pyfiglet
from termcolor import colored
from models import Session, helper
from models.display_tables import artist_table, venue_table, booking_table


session = Session()


def welcome_banner():
    banner = pyfiglet.figlet_format("Welcome!", font="slant")
    color_banner = colored(banner, "green")
    click.echo(color_banner)


def artist_banner():
    banner = pyfiglet.figlet_format("Artist", font="slant")
    color_banner = colored(banner, "red")
    click.echo(color_banner)


def venue_banner():
    banner = pyfiglet.figlet_format("Venue", font="slant")
    color_banner = colored(banner, "blue")
    click.echo(color_banner)


def booking_banner():
    banner = pyfiglet.figlet_format("Booking", font="slant")
    color_banner = colored(banner, "yellow")
    click.echo(color_banner)


def display_artist_table():
    artist_results = helper.get_all_artists()
    table = artist_table(artist_results)
    click.echo(table)


def display_venue_table():
    venue_results = helper.get_all_venues()
    table = venue_table(venue_results)
    click.echo(table)


def display_booking_table():
    booking_results = helper.get_all_bookings()
    table = booking_table(booking_results)
    click.echo(table)


def main():
    welcome_banner()
    while True:
        try:
            click.echo("\nOptions: ")
            click.echo("1. Display Artist, Venue and Booking Tables")
            click.echo("2. Create Artist Entry")
            click.echo("3. Update Artist Contact Information")
            click.echo("4. Remove Artist Entry")
            click.echo("5. Artist Availability")
            click.echo("6. Venue Capacity")
            click.echo("7. Update Venue Capacity")
            click.echo("8. Create Venue Entry")
            click.echo("9. Remove Venue Entry")
            click.echo("10. Create Booking Entry")
            click.echo("11. Update Booking Status")
            click.echo("12. Update Ticket Price")
            click.echo("13. Cancel Booking")

            choice = click.prompt(
                "Enter a number to select an option or 'q' to quit", type=str
            )

            if choice == "q":
                click.echo("Exiting...")
                break

            elif choice == "1":
                click.echo("\nDisplaying Artist, Venue and Booking...")
                artist_banner()
                display_artist_table()
                venue_banner()
                display_venue_table()
                booking_banner()
                display_booking_table()

            elif choice == "2":
                click.echo("\nCreating Artist Entry...")
                artist_banner()
                helper.create_artist_entry()

            elif choice == "3":
                click.echo("\nUpdating Artist Contact Information...")
                artist_banner()
                helper.update_artist_contact()

            elif choice == "4":
                click.echo("\nRemoving Artist Entry...")
                artist_banner()
                helper.remove_artist()

            elif choice == "5":
                click.echo("\nChecking Artist Availability...")
                artist_banner()
                helper.artist_availability()

            elif choice == "6":
                click.echo("\nChecking Venue Capacity...")
                venue_banner()
                helper.check_venue_capacity()

            elif choice == "7":
                click.echo("\nUpdating Venue Capacity")
                venue_banner()
                helper.update_venue_capacity()

            elif choice == "8":
                click.echo("\nCreating Venue Entry...")
                venue_banner()
                helper.create_new_venue()

            elif choice == "9":
                click.echo("\nRemoving Venue Entry...")
                booking_banner()
                helper.delete_venue()

            elif choice == "10":
                click.echo("\nCreating Booking Entry...")
                booking_banner()
                helper.create_booking()

            elif choice == "11":
                click.echo("\nUpdating Booking Status...")
                booking_banner()
                helper.update_booking_status()

            elif choice == "12":
                click.echo("\n Updating Ticket Price...")
                booking_banner()
                helper.update_ticket_price()

            elif choice == "13":
                click.echo("\nRemoving Booking Entry...")
                booking_banner()
                helper.cancel_booking()

            else:
                click.echo("\nInvalid choice. Try again")
        except Exception as e:
            click.echo(f"\nAn error occured {e}")


# @click.command()
# @click.option("--artist-name", prompt="Artist Name", help="Name of the Artist.")
# @click.option("--email", prompt="Artist email", help="Email for the Artist.")
# @click.option(
#     "--phone-number", prompt="Artist phone number", help="Phone number for the Artist"
# )
# @click.option("--address", prompt="Artist address", help="Address for the Artist.")
# @click.option("--city", prompt="Artist city", help="City of residence for the Artist.")
# @click.option(
#     "--state", prompt="Artist state", help="State of residence for the Artist."
# )
# @click.option(
#     "--zip-code",
#     prompt="Artist zip code",
#     help="Zip code of the residence for the Artist",
# )
# @click.option("--genre", prompt="Artist genre", help="Genre of music Artist plays")
# @click.option(
#     "--availability-str",
#     prompt="Artist availability",
#     help="Artist availability for booking",
# )
# def create_artist_entry(
#     artist_name,
#     email,
#     phone_number,
#     address,
#     city,
#     state,
#     zip_code,
#     genre,
#     availability_str,
# ):
#     helper.create_artist_entry(
#         artist_name,
#         email,
#         phone_number,
#         address,
#         city,
#         state,
#         zip_code,
#         genre,
#         availability_str,
#     )


# @click.command()
# @click.option(
#     "--artist-name", prompt="Artist name", help="Enter the name of the Artist"
# )
# @click.option(
#     "--new-email",
#     prompt="New email address",
#     help="Enter the new email address of the Artist",
# )
# @click.option(
#     "--new-phone-number",
#     prompt="New phone number",
#     help="Enter the new phone number of the Artist",
# )
# def update_artist_contact(artist_name, new_email, new_phone_number):
#     helper.update_artist_contact(artist_name, new_email, new_phone_number)


# @click.command()
# @click.option(
#     "--artist-name", prompt="Artist name", help="Enter the name of the Artist"
# )
# def remove_artist(artist_name):
#     helper.remove_artist(artist_name)


# @click.command()
# @click.option(
#     "--artist-name", prompt="Artist name", help="Enter the name of the Artist."
# )
# def artist_availability(artist_name):
#     helper.artist_availability(artist_name)


# @click.command()
# @click.option("--venue-name", prompt="Venue name", help="Enter the name of the Venue.")
# def check_venue_capacity(venue_name):
#     helper.check_venue_capacity(venue_name)


# @click.command()
# @click.option("--venue-name", prompt="Venue name", help="Enter the name of the Venue.")
# @click.option(
#     "--venue-email", prompt="Venue email", help="Enter the email used by the Venue."
# )
# @click.option(
#     "--venue-city", prompt="Venue city", help="Enter the city location of the Venue."
# )
# @click.option(
#     "--venue-state", prompt="Venue state", help="Enter the state location of the Venue."
# )
# @click.option(
#     "--venue-zip-code",
#     prompt="Venue zip code",
#     help="Enter the zip code location for the venue.",
# )
# @click.option("--capacity", prompt="Capacity", help="Enter the capacity of the Venue.")
# def create_new_venue(
#     venue_name, venue_email, venue_city, venue_state, venue_zip_code, capacity
# ):
#     helper.create_new_venue(
#         venue_name, venue_email, venue_city, venue_state, venue_zip_code, capacity
#     )


# @click.command()
# @click.option("--venue-name", prompt="Venue name", help="Enter the venue Vame.")
# def delete_venue(venue_name):
#     helper.delete_venue(venue_name)


# @click.command()
# @click.option(
#     "--artist-name", prompt="Artist name", help="Enter the name of the Artist."
# )
# @click.option(
#     "--booking-date-str", prompt="Booking date", help="Enter the date of the Booking."
# )
# @click.option(
#     "--ticket-price", prompt="Ticket price", help="Enter the price of the ticket."
# )
# @click.option("--venue-name", prompt="Venue name", help="Enter the name of the Venue.")
# def create_booking(artist_name, booking_date_str, ticket_price, venue_name):
#     helper.create_booking(artist_name, booking_date_str, ticket_price, venue_name)


# @click.command()
# @click.option(
#     "--artist-name", prompt="Artist name", help="Enter the name of the Artist"
# )
# @click.option("--venue-name", prompt="Venue name")
# @click.option("--booking-date-str", prompt="Booking date")
# def cancel_booking(artist_name, venue_name, booking_date_str):
#     helper.cancel_booking(artist_name, venue_name, booking_date_str)


# @click.command()
# @click.option(
#     "--artist-name", prompt="Artist name", help="Enter the name of the Artist"
# )
# @click.option(
#     "--booking-date-str", prompt="Booking date", help="Enter the date of the Booking"
# )
# @click.option(
#     "--new-status", prompt="Enter Status", help="Enter Confirmed or Pending for status"
# )
# def update_booking_status(artist_name, booking_date_str, new_status):
#     helper.update_booking_status(artist_name, booking_date_str, new_status)


# cli.add_command(display_artist_table)
# cli.add_command(display_venue_table)
# cli.add_command(display_booking_table)
# cli.add_command(create_artist_entry)
# cli.add_command(update_artist_contact)
# cli.add_command(remove_artist)
# cli.add_command(check_venue_capacity)
# cli.add_command(create_new_venue)
# cli.add_command(delete_venue)
# cli.add_command(create_booking)
# cli.add_command(cancel_booking)


if __name__ == "__main__":
    main()
