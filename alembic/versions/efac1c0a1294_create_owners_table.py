"""create owners table

Revision ID: efac1c0a1294
Revises: 0ec384adb82b
Create Date: 2022-01-22 21:08:03.348555

"""
from alembic import op
from sqlalchemy import Column, ForeignKey
import sqlalchemy.dialects.postgresql as sa


# revision identifiers, used by Alembic.
revision = 'efac1c0a1294'
down_revision = '0ec384adb82b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'owners',
        Column('id', sa.UUID, primary_key=True),
        Column('first_name', sa.VARCHAR(100), nullable=False),
        Column('last_name', sa.VARCHAR(100), nullable=False),
        Column('email', sa.VARCHAR(100), nullable=False)
    )

    op.add_column('properties',
        Column('owner_id', sa.UUID, ForeignKey('owners.id'), nullable=False)
    )


def downgrade():
    op.drop_column('properties', 'owner_id')
    op.drop_table('owners')
