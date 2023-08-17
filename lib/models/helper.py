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


def update_artist_contact():
    ##filter by artist email, phone_number
    ##allow artist to update email, phone_number
    ## return confirmed
    pass


def remove_artist():
    ##query by artist name
    ## if name matches remove
    pass


def find_by_availability():
    ##filter by availability date
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
