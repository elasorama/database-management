"""Added the power consumption table

Revision ID: 82ca074f7e48
Revises: 53f7b7ed247c
Create Date: 2024-01-21 17:44:54.494274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82ca074f7e48'
down_revision: Union[str, None] = '53f7b7ed247c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('power_consumption',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('power_usage_5_minutes_ahead', sa.Float(), nullable=True),
    sa.Column('power_usage_15_minutes_ahead', sa.Float(), nullable=True),
    sa.Column('power_usage_60_minutes_ahead', sa.Float(), nullable=True),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('updated_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('power_consumption')
    # ### end Alembic commands ###