"""empty message

Revision ID: 87f01ae5266c
Revises: 35793c5f042f
Create Date: 2020-06-08 10:25:29.379246

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '87f01ae5266c'
down_revision = '35793c5f042f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('time', mysql.TIME(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appointments', 'time')
    # ### end Alembic commands ###