from models import Session, Artist, Venue, Booking
from datetime import datetime

import click

session = Session()


# query by all artists
# helper for artist table
def get_all_artists():
    artists = session.query(Artist).all()
    return artists


# query by all venues
# helper for venues table
def get_all_venues():
    venues = session.query(Venue).all()
    return venues


# query by all bookings
# helper for booking table
def get_all_bookings():
    bookings = session.query(Booking).all()
    return bookings


##query by artist name
## if artist name available, create new artist entry
def create_artist_entry():
    artist_name = click.prompt("Artist Name")
    email = click.prompt("Email")
    phone_number = click.prompt("Phone")
    address = click.prompt("Address")
    city = click.prompt("City")
    state = click.prompt("State")
    zip_code = click.prompt("Zip")
    genre = click.prompt("Genre")
    availability_str = click.prompt("Availability")

    existing_artist = session.query(Artist).filter_by(artist_name=artist_name).first()

    if existing_artist is None:
        availability = datetime.strptime(availability_str, "%Y-%m-%d").date()

        new_artist = Artist(
            artist_name=artist_name,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            genre=genre,
            availability=availability,
        )
        session.add(new_artist)
        session.commit()

        click.echo(f"Artist: {artist_name} created!")
    else:
        click.echo(f"Artist: {artist_name} already exists")


# filter by artist name
# allow artist to update email, phone_number
# return confirmed
def update_artist_contact():
    artist_name = click.prompt("Artist Name")
    new_email = click.prompt("Email")
    new_phone_number = click.prompt("Phone Number")

    update_existing_artist = (
        session.query(Artist).filter_by(artist_name=artist_name).first()
    )

    if update_existing_artist:
        update_existing_artist.email = new_email
        update_existing_artist.phone_number = new_phone_number

        click.echo(
            f"Artist: {artist_name} contact information has been updated successfully!"
        )

        session.add(update_existing_artist)
        session.commit()

    else:
        click.echo(f"Artist: {artist_name} not found!")


# query by artist name
# if name matches remove
def remove_artist():
    artist_name = click.prompt("Enter the Artist Name")
    remove_current_artist = (
        session.query(Artist).filter_by(artist_name=artist_name).first()
    )

    if remove_current_artist:
        artist_id = remove_current_artist.id

        bookings_to_remove = session.query(Booking).filter_by(artist_id=artist_id).all()

        for booking in bookings_to_remove:
            session.delete(booking)

        session.delete(remove_current_artist)
        session.commit()

        click.echo(f"Artist: {artist_name} removed!")
    else:
        click.echo(f"Artist: {artist_name} does not exist. Try again!")


##filter by availability date and artist name
## if date matches return message available
def artist_availability():
    artist_name = click.prompt("Artist Name")

    check_artist_availability = (
        session.query(Artist).filter_by(artist_name=artist_name).first()
    )

    if check_artist_availability:
        session.commit()
        click.echo(
            f"Artist: {artist_name} is available on {check_artist_availability.availability}"
        )
    else:
        click.echo(
            f"Artist: {artist_name} is not available on {check_artist_availability.availability}"
        )


## query venue by name and capacity
## allow check of venue capacity
def check_venue_capacity():
    venue_name = click.prompt("Venue Name")
    venue = session.query(Venue).filter_by(venue_name=venue_name).first()

    if venue:
        session.commit()

        click.echo(
            f"Venue: {venue_name} has {venue.capacity} seats available for seating"
        )
    else:
        click.echo(f"Venue: Unable to find {venue_name} provided")


##query venue by name and capacity
##update venue capacity
def update_venue_capacity():
    venue_name = click.prompt("Venue Name")
    capacity = click.prompt("Capacity")
    new_capacity = click.prompt("New Capacity")

    current_venue_capacity = (
        session.query(Venue).filter_by(venue_name=venue_name, capacity=capacity).first()
    )

    if current_venue_capacity:
        current_venue_capacity.capacity = new_capacity
        click.echo(
            f"Venue: {venue_name} has been updated to {new_capacity} for seating capacity."
        )

        session.commit()

    else:
        click.echo(f"Venue: {venue_name} capacity has not been updated.")


# filter by venue name
# if venue name is available create new venue
def create_new_venue():
    venue_name = click.prompt("Venue Name")
    venue_email = click.prompt("Email")
    venue_city = click.prompt("City")
    venue_state = click.prompt("State")
    venue_zip_code = click.prompt("Zip")
    capacity = click.prompt("Capacity")

    existing_venue = session.query(Venue).filter_by(venue_name=venue_name).first()

    if existing_venue is None:
        new_venue = Venue(
            venue_name=venue_name,
            venue_email=venue_email,
            venue_city=venue_city,
            venue_state=venue_state,
            venue_zip_code=venue_zip_code,
            capacity=capacity,
        )

        session.add(new_venue)
        session.commit()

        print(f"Venue: {venue_name} created!")
    else:
        print(f"Venue: {venue_name} already exists!")


# filter by venue name
# if venue available, remove venue
def delete_venue():
    venue_name = click.prompt("Venue Name")
    venue_to_delete = session.query(Venue).filter_by(venue_name=venue_name).first()

    if venue_to_delete:
        bookings = session.query(Booking).filter_by(venue_id=venue_to_delete.id).all()
        for booking in bookings:
            session.delete(booking)

        session.delete(venue_to_delete)
        session.commit()

        print(f"Venue: {venue_name} has been deleted!")
    else:
        print(f"Venue: {venue_name} does not exist.")


# query by status and booking date
# if booking status false, allow for booking
# otherwise, return message booking not created
def create_booking():
    artist_name = click.prompt("Artist Name")
    booking_date_str = click.prompt("Booking Date")
    ticket_price = click.prompt("Ticket Price")
    venue_name = click.prompt("Venue Name")
    status = click.prompt("Status")
    artist = session.query(Artist).filter_by(artist_name=artist_name).first()

    if not artist:
        print(f"Artist: {artist_name} does not exist! Booking not created.")
        return

    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()
    venue = session.query(Venue).filter_by(venue_name=venue_name).first()

    if not venue:
        click.echo(f"Venue: {venue_name} does not exist!")
        return

    existing_booking = (
        session.query(Booking)
        .filter_by(artist_id=artist.id, booking_date=booking_date)
        .first()
    )

    if existing_booking:
        click.echo(f"Booking for {artist_name} already exists on {booking_date}")
    else:
        new_booking = Booking(
            artist=artist,
            booking_date=booking_date,
            ticket_price=ticket_price,
            venue=venue,
            status=status,
        )
        session.add(new_booking)
        session.commit()

        click.echo(
            f"Booking created successfully. {artist_name} booked for {booking_date}"
        )


# query by booking_date, artist name
# update status from "Pending" to "Confirmed" or vice versa
def update_booking_status():
    artist_name = click.prompt("Artist Name")
    booking_date_str = click.prompt("Booking Date")
    new_status = click.prompt("New Status")

    artist = session.query(Artist).filter_by(artist_name=artist_name).first()

    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()

    if artist:
        booking = (
            session.query(Booking)
            .filter(
                Booking.artist_id == artist.id, Booking.booking_date == booking_date
            )
            .first()
        )

        if booking:
            booking.status = new_status
            session.commit()

        click.echo(
            f"Status: {new_status}. Status updated successfully for {artist_name} on {booking_date_str}"
        )
    else:
        click.echo(
            f"Status: Status not updated. {artist_name} booking on {booking_date_str} not found"
        )


# query by booking_date
# update price
def update_ticket_price():
    pass


# query by booking_date, artist name
# remove booking, return message that confirmed
def cancel_booking():
    artist_name = click.prompt("Artist Name")
    venue_name = click.prompt("Venue Name")
    booking_date_str = click.prompt("Booking Date")

    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()

    find_by_current_booking = (
        session.query(Booking)
        .filter(
            Booking.artist.has(artist_name=artist_name),
            Booking.venue.has(venue_name=venue_name),
            Booking.booking_date == booking_date,
        )
        .one_or_none()
    )

    if find_by_current_booking:
        session.delete(find_by_current_booking)
        session.commit()
        print(
            f"Booking: {artist_name} booked on {booking_date} at {venue_name} has been deleted."
        )
    else:
        print(f"Booking: {artist_name} not found for {booking_date} at {venue_name}.")
