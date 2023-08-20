from models import Session, Artist, Venue, Booking
from sqlalchemy.orm import joinedload
from datetime import datetime

session = Session()


##query by artist name
## if artist name available, create new artist entry
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
        print(f"Artist: {artist_name} created!")
    else:
        print(f"Artist: {artist_name} already exists")


# filter by artist name
# allow artist to update email, phone_number
# return confirmed
def update_artist_contact(artist_name, new_email, new_phone_number):
    update_existing_artist = (
        session.query(Artist).filter_by(artist_name=artist_name).first()
    )

    if update_existing_artist:
        update_existing_artist.email = new_email
        update_existing_artist.phone_number = new_phone_number

        print(
            f"Artist: {artist_name} contact information has been updated successfully!"
        )

        session.add(update_existing_artist)
        session.commit()

    else:
        print(f"Artist: {artist_name} not found!")


# query by artist name
# if name matches remove
def remove_artist(artist_name):
    remove_current_artist = (
        session.query(Artist).filter_by(artist_name=artist_name).first()
    )

    if remove_current_artist:
        session.delete(remove_current_artist)
        session.commit()

        print(f"Artist: {artist_name} removed!")
    else:
        print(f"Artist: {artist_name} does not exist. Try again!")


##filter by availability date and artist name
## if date matches return message available
def artist_availability(artist_name, availability):
    check_artist_availability = (
        session.query(Artist)
        .filter_by(artist_name=artist_name, availability=availability)
        .first()
    )

    if check_artist_availability:
        session.commit()
        print(f"Artist: {artist_name} is available on {availability}")
    else:
        print(f"Artist: {artist_name} is not available on {availability}")


## query venue by name and capacity
## allow check of venue capacity
def check_venue_capacity(venue_name, capacity):
    check_venue_capacity = (
        session.query(Venue).filter_by(venue_name=venue_name, capacity=capacity).first()
    )

    if check_venue_capacity:
        session.commit()

        print(f"Venue: {venue_name} has {capacity} seats available for seating")
    else:
        print(f"Venue: Unable to find {venue_name} with {capacity} seating provided")


##query venue by name and capacity
##update venue capacity
def update_venue_capacity(venue_name, capacity, new_capacity):
    current_venue_capacity = (
        session.query(Venue).filter_by(venue_name=venue_name, capacity=capacity).first()
    )

    if current_venue_capacity:
        current_venue_capacity.capacity = new_capacity
        print(
            f"Venue: {venue_name} has been updated to {new_capacity} for seating capacity."
        )

        session.commit()

    else:
        print(f"Venue: {venue_name} capacity has not been updated.")


# filter by venue name
# if venue name is available create new venue
def create_new_venue(
    venue_name, venue_email, venue_city, venue_state, venue_zip_code, capacity
):
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
def delete_venue(venue_name):
    venue_to_delete = session.query(Venue).filter_by(venue_name=venue_name).first()

    if venue_to_delete:
        session.delete(venue_to_delete)
        session.commit()

        print(f"Venue: {venue_name} has been deleted!")
    else:
        print(f"Venue: {venue_name} does not exist.")


# query by status and booking date
# if booking status false, allow for booking
# otherwise, return message booking not created
def create_booking(artist_name, booking_date_str, venue_name):
    artist = session.query(Artist).filter_by(artist_name=artist_name).first()

    if not artist:
        print(f"Artist: {artist_name} does not exist! Booking not created.")
        return

    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()
    venue = session.query(Venue).filter_by(venue_name=venue_name).first()

    if not venue:
        print(f"Venue: {venue_name} does not exist!")
        return

    existing_booking = (
        session.query(Booking)
        .filter_by(artist=artist, booking_date=booking_date)
        .first()
    )

    if existing_booking:
        print(f"Booking for {artist_name} already exists on {booking_date}")
    else:
        new_booking = Booking(
            artist=artist,
            status=True,
            booking_date=booking_date,
            venue=venue,
        )
        session.add(new_booking)
        session.commit()

        print(f"Booking created successfully. {artist_name} booked for {booking_date}")


# query by booking_date, artist name
# remove booking, return message that confirmed
def cancel_booking(
    artist_name,
    venue_name,
    booking_date_str,
):
    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()

    find_by_current_booking = (
        session.query(Booking)
        .join(Artist, Artist.id == Booking.artist_id)
        .join(Venue, Venue.id == Booking.venue_id)
        .filter(
            Artist.artist_name == artist_name,
            Venue.venue_name == venue_name,
            Booking.booking_date == booking_date,
        )
        .options(joinedload(Booking.artist), joinedload(Booking.venue))
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


# if true:
# return message that venue is booked
# otherwise, return message that venue is available
def confirmed_booking():
    pass
