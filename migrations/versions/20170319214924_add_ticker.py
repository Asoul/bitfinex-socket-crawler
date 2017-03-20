"""Add ticker

Revision ID: 8cb7c97337cc
Revises:
Create Date: 2017-03-19 21:49:24.479975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cb7c97337cc'
down_revision = None
branch_labels = None
depends_on = None

currency_list = [
    'btc', 'eth', 'etc', 'bfx', 'zec', 'xmr', 'ltc', 'dsh', 'rrt', 'bcc', 'bcu'
]

def upgrade():
    for currency in currency_list:
        op.create_table(
            '{}_ticker'.format(currency),
            sa.Column('timestamp', sa.BigInteger, primary_key=True),
            sa.Column('bid_price', sa.Float),
            sa.Column('bid_size', sa.Float),
            sa.Column('ask_price', sa.Float),
            sa.Column('ask_size', sa.Float),
            sa.Column('daily_change', sa.Float),
            sa.Column('daily_change_perc', sa.Float),
            sa.Column('last_price', sa.Float),
            sa.Column('daily_volume', sa.Float),
            sa.Column('daily_high', sa.Float),
            sa.Column('daily_low', sa.Float)
        )

def downgrade():
    for currency in currency_list:
        op.drop_table('{}_ticker'.format(currency))
