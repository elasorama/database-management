"""Added status code logging

Revision ID: bcb853436519
Revises: b4067adf9f8c
Create Date: 2024-01-21 21:12:08.450590

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bcb853436519'
down_revision: Union[str, None] = 'b4067adf9f8c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_power_usage', sa.Column('response_status_code', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('api_power_usage', 'response_status_code')
    # ### end Alembic commands ###
