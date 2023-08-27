#!/usr/bin/env python
import click
import pyfiglet
from termcolor import colored
from models import Session, helper
from models.display_tables import artist_table, venue_table, booking_table


session = Session()


def clear_screen():
    print("\n" * 40)


def welcome_banner():
    banner = pyfiglet.figlet_format("Welcome to Booked!", font="slant")
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
                clear_screen()
                click.echo("\nDisplaying Artist, Venue and Booking...")
                artist_banner()
                display_artist_table()
                venue_banner()
                display_venue_table()
                booking_banner()
                display_booking_table()

            elif choice == "2":
                clear_screen()
                click.echo("\nCreating Artist Entry...")
                artist_banner()
                helper.create_artist_entry()
                clear_screen()

            elif choice == "3":
                clear_screen()
                click.echo("\nUpdating Artist Contact Information...")
                artist_banner()
                helper.update_artist_contact()

            elif choice == "4":
                clear_screen()
                click.echo("\nRemoving Artist Entry...")
                artist_banner()
                helper.remove_artist()

            elif choice == "5":
                clear_screen()
                click.echo("\nChecking Artist Availability...")
                artist_banner()
                helper.artist_availability()

            elif choice == "6":
                clear_screen()
                click.echo("\nChecking Venue Capacity...")
                venue_banner()
                helper.check_venue_capacity()

            elif choice == "7":
                clear_screen()
                click.echo("\nUpdating Venue Capacity")
                venue_banner()
                helper.update_venue_capacity()

            elif choice == "8":
                clear_screen()
                click.echo("\nCreating Venue Entry...")
                venue_banner()
                helper.create_new_venue()

            elif choice == "9":
                clear_screen()
                click.echo("\nRemoving Venue Entry...")
                booking_banner()
                helper.delete_venue()

            elif choice == "10":
                clear_screen()
                click.echo("\nCreating Booking Entry...")
                booking_banner()
                helper.create_booking()

            elif choice == "11":
                clear_screen()
                click.echo("\nUpdating Booking Status...")
                booking_banner()
                helper.update_booking_status()

            elif choice == "12":
                clear_screen()
                click.echo("\n Updating Ticket Price...")
                booking_banner()
                helper.update_ticket_price()

            elif choice == "13":
                clear_screen()
                click.echo("\nRemoving Booking Entry...")
                booking_banner()
                helper.cancel_booking()

            else:
                click.echo("\nInvalid choice. Try again")
        except Exception as e:
            click.echo(f"\nAn error occured {e}")


if __name__ == "__main__":
    main()
