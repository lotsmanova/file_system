"""add model user

Revision ID: 0266a3daf4f8
Revises: 
Create Date: 2024-02-03 17:00:19.308738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0266a3daf4f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)



def downgrade() -> None:
    pass
