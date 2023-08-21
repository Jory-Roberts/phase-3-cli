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
        click.echo("3. Exit")

        choice = input("Enter a number to select an option: ")

        if choice == "1":
            click.echo("Creating Artist Entry...")
            create_artist_entry()
        elif choice == "2":
            click.echo("Updating Artist Contact Information...")
            update_artist_contact()
        elif choice == "3":
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

    cli.add_command(create_artist_entry)
    cli.add_command(update_artist_contact)


if __name__ == "__main__":
    cli()
