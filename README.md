# Booked! App

![CLIOptions](/Images/CLI%20Options.png)

## Inspiration

My idea for Booked! is quite simple: Music scenes are large and diverse across metropolitan areas. This app hopes to streamline that process. Whether you're a venue owner or an artist, the ability to quickly book a show should come with as few possible headaches so you can get back to rocking the stage. Enjoy!

## Project Design

![Phase3Schema](/Images/Phase%203%20Project%20Schema%20Music%20Venue.png)

The design features 3 tables for reference: Artist, Venue and Booking. I intended the Booking table to act like an association table, but I added a booking date along with a ticket price and status columns. This helps maintain my many-to-many relationship. Eventually, I would like to expand this project and allow for users to designate whether they are an 'artist' or 'venue owner'.

## Project Structure

You can view the tree structure under the `filetree.txt` included in the lib directory. For a brief rundown:

- `lib` is the main directory
- `models` is the home for all relevent classes (`Artist`, `Venue`, `Booking`)
- `helper` houses all relevent methods for those classes

## Installation

Installation is straightforward.

1. Fork and clone `Phase-3-CLI` repo to your local machine
2. Navigate into the project directory
3. If you don't have `pipenv` installed, you can do so by `pip install pipenv`
4. Run `pipenv install`

## Dependencies

The following packages will be installed when you run `pipenv install`:

- alembic
- sqlalchemy (==1.4.41)
- faker
- click
- ipdb
- prettytable
- termcolor
- pyfiglet

## Notes

After installing the dependencies:

1. Run `pipenv shell` to enter the virtual environment
2. Navigate to the main directory with `cd lib`
3. Initialize the schema by running `alembic upgrade head`
4. Populate the tables with `python seeds.py`
5. Run `python debug.py` to run the methods in a test environment. You can run an `import from models` and bring in any or all of the classes (Artist, Booking, Table)

These steps will set up the database and populate it with initial data
