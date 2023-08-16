"""drop tables

Revision ID: 13dddc4fbf0e
Revises: 2af05c978204
Create Date: 2023-08-15 22:47:15.396464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "13dddc4fbf0e"
down_revision = "2af05c978204"
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
