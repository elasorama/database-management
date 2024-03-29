"""Added the upgraded and created datetime columns

Revision ID: 53f7b7ed247c
Revises: a3ed4a1f8173
Create Date: 2024-01-21 17:31:37.991448

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53f7b7ed247c'
down_revision: Union[str, None] = 'a3ed4a1f8173'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('electricity_timeseries', sa.Column('created_datetime', sa.DateTime(), nullable=True))
    op.add_column('electricity_timeseries', sa.Column('updated_datetime', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('electricity_timeseries', 'updated_datetime')
    op.drop_column('electricity_timeseries', 'created_datetime')
    # ### end Alembic commands ###
