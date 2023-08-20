"""drop tables add artist name venue name to Booking

Revision ID: 80d30be9685d
Revises: 06bb7ca12796
Create Date: 2023-08-19 20:30:22.772463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "80d30be9685d"
down_revision = "06bb7ca12796"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table("booking")
    op.drop_table("venue")
    op.drop_table("artist")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
