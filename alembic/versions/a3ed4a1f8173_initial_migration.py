"""Initial migration

Revision ID: a3ed4a1f8173
Revises: 
Create Date: 2024-01-21 17:30:03.406439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3ed4a1f8173'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('electricity_timeseries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('power_usage', sa.Float(), nullable=True),
    sa.Column('current', sa.Float(), nullable=True),
    sa.Column('voltage', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('electricity_timeseries')
    # ### end Alembic commands ###
