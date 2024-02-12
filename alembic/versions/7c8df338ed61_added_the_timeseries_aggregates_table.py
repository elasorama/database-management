"""Added the timeseries aggregates table

Revision ID: 7c8df338ed61
Revises: 076f7d91052d
Create Date: 2024-02-02 22:15:34.092618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c8df338ed61'
down_revision: Union[str, None] = '076f7d91052d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timeseries_aggregated',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.Column('metric', sa.String(), nullable=True),
    sa.Column('n_ahead', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('created_datetime', sa.DateTime(), nullable=True),
    sa.Column('updated_datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timeseries_aggregated')
    # ### end Alembic commands ###
