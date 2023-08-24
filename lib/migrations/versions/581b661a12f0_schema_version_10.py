"""schema version 10

Revision ID: 581b661a12f0
Revises: 72bab9c35505
Create Date: 2023-08-22 08:46:40.992773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '581b661a12f0'
down_revision = '72bab9c35505'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('availability', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('venue_name', sa.String(), nullable=True),
    sa.Column('venue_email', sa.String(), nullable=True),
    sa.Column('venue_city', sa.String(), nullable=True),
    sa.Column('venue_state', sa.String(), nullable=True),
    sa.Column('venue_zip_code', sa.String(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('venue_email')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('booking_date', sa.Date(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    op.drop_table('venue')
    op.drop_table('artist')
    # ### end Alembic commands ###