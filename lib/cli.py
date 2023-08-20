#!/usr/bin/env python
import click
from models import Artist, Booking, Venue, Session, helper


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
def cli_create_artist_entry(
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


if __name__ == "__main__":
    cli_create_artist_entry()
