"""empty message

Revision ID: dd7c7859d260
Revises: 080d8677d642
Create Date: 2020-06-24 13:18:48.299728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd7c7859d260'
down_revision = '080d8677d642'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('source_language', sa.String(length=100), nullable=True),
    sa.Column('target_languages', sa.Text(), nullable=False),
    sa.Column('industry', sa.String(length=150), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('time', sa.TIME(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('join_url', sa.String(length=256), nullable=True),
    sa.Column('start_url', sa.String(length=550), nullable=True),
    sa.Column('meeting_id', sa.String(length=15), nullable=True),
    sa.Column('meeting_password', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    # ### end Alembic commands ###
