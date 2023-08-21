#!/usr/bin/env python
import click
from models import Artist, Booking, Venue, Session, helper


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """CLI for managing venue and artist information"""
    if ctx.invoked_subcommand is None:
        user_menu()


def user_menu():
    while True:
        click.echo("\nOptions: ")
        click.echo("1. Create Artist Entry")
        click.echo("2. Update Artist Contact Information")
        click.echo("3. Remove Artist Entry")
        click.echo("4. Artist Availability")
        click.echo("5. Venue Capacity")
        click.echo("9. Exit")

        choice = input("Enter a number to select an option: ")

        if choice == "1":
            click.echo("Creating Artist Entry...")
            create_artist_entry()
        elif choice == "2":
            click.echo("Updating Artist Contact Information...")
            update_artist_contact()
        elif choice == "3":
            click.echo("Removing Artist Entry...")
            remove_artist()
        elif choice == "4":
            click.echo("Checking Artist Availability...")
            artist_availability()
        elif choice == "5":
            click.echo("Checking Venue Capacity...")
            check_venue_capacity()
        elif choice == "9":
            click.echo("Exiting...")
            break


@click.command()
@click.option("--artist-name", prompt="Artist Name", help="Name of the Artist.")
@click.option("--email", prompt="Artist email", help="Email for the Artist.")
@click.option(
    "--phone-number", prompt="Artist phone number", help="Phone number for the Artist"
)
@click.option("--address", prompt="Artist address", help="Address for the Artist.")
@click.option("--city", prompt="Artist city", help="City of residence for the Artist.")
@click.option(
    "--state", prompt="Artist state", help="State of residence for the Artist."
)
@click.option(
    "--zip-code",
    prompt="Artist zip code",
    help="Zip code of the residence for the Artist",
)
@click.option("--genre", prompt="Artist genre", help="Genre of music Artist plays")
@click.option(
    "--availability-str",
    prompt="Artist availability",
    help="Artist availability for booking",
)
def create_artist_entry(
    artist_name,
    email,
    phone_number,
    address,
    city,
    state,
    zip_code,
    genre,
    availability_str,
):
    helper.create_artist_entry(
        artist_name,
        email,
        phone_number,
        address,
        city,
        state,
        zip_code,
        genre,
        availability_str,
    )


@click.command()
@click.option(
    "--artist-name", prompt="Artist name", help="Enter the name of the Artist"
)
@click.option(
    "--new-email",
    prompt="New email address",
    help="Enter the new email address of the Artist",
)
@click.option(
    "--new-phone-number",
    prompt="New phone number",
    help="Enter the new phone number of the Artist",
)
def update_artist_contact(artist_name, new_email, new_phone_number):
    helper.update_artist_contact(artist_name, new_email, new_phone_number)


@click.command()
@click.option(
    "--artist-name", prompt="Artist name", help="Enter the name of the Artist"
)
def remove_artist(artist_name):
    helper.remove_artist(artist_name)


@click.command()
@click.option(
    "--artist-name", prompt="Artist name", help="Enter the name of the Artist."
)
@click.option(
    "--availability",
    prompt="Artist availability",
    help="Enter the booking availability for the Artist",
)
def artist_availability(artist_name, availability):
    helper.artist_availability(artist_name, availability)


@click.command()
@click.option("--venue-name", prompt="Venue name", help="Enter the name of the venue.")
@click.option("--capacity", prompt="Venue capacity", help="Enter the venue capacity")
def check_venue_capacity(venue_name, capacity):
    helper.check_venue_capacity(venue_name, capacity)

    cli.add_command(create_artist_entry)
    cli.add_command(update_artist_contact)
    cli.add_command(remove_artist)
    cli.add_command(check_venue_capacity)


if __name__ == "__main__":
    cli()
