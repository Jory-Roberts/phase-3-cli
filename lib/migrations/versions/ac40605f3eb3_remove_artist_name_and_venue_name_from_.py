"""Remove artist_name and venue_name from Booking

Revision ID: ac40605f3eb3
Revises: 51a04dd97d8b
Create Date: 2023-08-19 22:40:51.795247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ac40605f3eb3"
down_revision = "51a04dd97d8b"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("booking", "artist_name")
    op.drop_column("booking", "venue_name")


def downgrade():
    op.add_column("booking", sa.Column("artist_name", sa.String()))
    op.add_column("booking", sa.Column("venue_name", sa.String()))
