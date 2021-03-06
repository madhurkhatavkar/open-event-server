"""empty message

Revision ID: be959d7b84d4
Revises: 57a62630eeea
Create Date: 2020-08-27 12:51:55.332596

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'be959d7b84d4'
down_revision = '57a62630eeea'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('live_stream_url', sa.String(), nullable=True))
    op.add_column('events', sa.Column('webinar_url', sa.String(), nullable=True))
    op.add_column('events_version', sa.Column('live_stream_url', sa.String(), autoincrement=False, nullable=True))
    op.add_column('events_version', sa.Column('webinar_url', sa.String(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events_version', 'webinar_url')
    op.drop_column('events_version', 'live_stream_url')
    op.drop_column('events', 'webinar_url')
    op.drop_column('events', 'live_stream_url')
    # ### end Alembic commands ###
