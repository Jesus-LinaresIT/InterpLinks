"""empty message

Revision ID: e98266c75b2d
Revises: c139e7e136e6
Create Date: 2020-06-01 11:03:24.337034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e98266c75b2d'
down_revision = 'c139e7e136e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_language', sa.String(length=100), nullable=True),
    sa.Column('target_languages', sa.Text(), nullable=False),
    sa.Column('industry', sa.String(length=150), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appointments')
    # ### end Alembic commands ###
