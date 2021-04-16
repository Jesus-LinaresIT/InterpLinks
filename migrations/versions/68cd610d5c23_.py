"""empty message

Revision ID: 68cd610d5c23
Revises: 49920d8a8e35
Create Date: 2020-06-09 12:15:22.301579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68cd610d5c23'
down_revision = '49920d8a8e35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('userId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'appointments', 'users', ['userId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.drop_column('appointments', 'userId')
    # ### end Alembic commands ###