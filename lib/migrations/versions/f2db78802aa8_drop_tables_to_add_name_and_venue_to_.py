"""drop tables to add name and venue to Booking

Revision ID: f2db78802aa8
Revises: ac40605f3eb3
Create Date: 2023-08-21 14:04:39.585311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f2db78802aa8"
down_revision = "ac40605f3eb3"
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
