"""empty message

Revision ID: e2c5dbcf0f21
Revises: 6cf922c46545
Create Date: 2016-10-03 02:27:42.548590

"""

# revision identifiers, used by Alembic.
revision = 'e2c5dbcf0f21'
down_revision = '6cf922c46545'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('_hashed_password', sa.String(), nullable=True))
    op.drop_column('users', '_password')
    op.drop_column('users', '_salt')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('_salt', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('_password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', '_hashed_password')
    ### end Alembic commands ###
