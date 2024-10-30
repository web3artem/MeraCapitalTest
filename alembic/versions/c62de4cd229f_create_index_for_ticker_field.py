"""create index for ticker field

Revision ID: c62de4cd229f
Revises: 3dce24d4583e
Create Date: 2024-10-30 21:04:57.698784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c62de4cd229f'
down_revision: Union[str, None] = '3dce24d4583e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_currency_ticker', 'currency', ['ticker'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_currency_ticker', table_name='currency')
    # ### end Alembic commands ###