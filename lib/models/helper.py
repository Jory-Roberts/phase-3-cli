from models import Session, Artist, Venue, Booking
from datetime import datetime


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
    session = Session()

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


##filter by artist name
##allow artist to update email, phone_number
## return confirmed
def update_artist_contact(artist_name, new_email, new_phone_number):
    session = Session()

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


##query by artist name
## if name matches remove
def remove_artist(artist_name):
    session = Session()
    remove_current_artist = (
        session.query(Artist).filter_by(artist_name=artist_name).first()
    )

    if remove_current_artist:
        session.delete(remove_current_artist)
        session.commit()
        print(f"Artist: {artist_name} removed!")
    else:
        print(f"Artist: {artist_name} does not exist. Try again!")


def artist_availability():
    ##filter by availability date and artist name
    ## if date matches return message available
    pass


def update_venue_capacity():
    ## query venue by capacity
    ## allow update of venue capacity
    pass


def create_new_venue():
    ##filter by venue name
    ## if venue name is available create new venue
    pass


def delete_venue():
    ## filter by venue name
    ## if venue available, remove venue
    pass


def create_booking():
    ##query by status and booking date
    ## if booking status false, allow for booking
    ## otherwise, return message booking not created
    pass


def cancel_booking():
    ##query by booking_date
    ## remove booking, return message that confirmed
    pass


def confirmed_booking():
    ##if true:
    ## return message that venue is booked
    ## otherwise, return message that venue is available
    pass
