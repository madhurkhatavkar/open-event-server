"""empty message

Revision ID: 167379522d3d
Revises: 06e3dc4e8d68
Create Date: 2016-06-11 23:47:40.027113

"""

# revision identifiers, used by Alembic.
revision = '167379522d3d'
down_revision = '06e3dc4e8d68'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_detail', sa.Column('details', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_detail', 'details')
    ### end Alembic commands ###
