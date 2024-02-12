"""Only leaving the timeseries table

Revision ID: 076f7d91052d
Revises: 7a5ac00bd997
Create Date: 2024-02-02 21:26:57.167080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '076f7d91052d'
down_revision: Union[str, None] = '7a5ac00bd997'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timeseries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('metric', sa.String(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('updated_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('electricity_timeseries')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('electricity_timeseries',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('power_usage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('current', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('voltage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='electricity_timeseries_pkey')
    )
    op.drop_table('timeseries')
    # ### end Alembic commands ###