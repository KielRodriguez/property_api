"""create property table

Revision ID: 0ec384adb82b
Revises: 
Create Date: 2022-01-14 00:35:12.663230

"""
from alembic import op
from sqlalchemy import Column
import sqlalchemy.dialects.postgresql as sa


# revision identifiers, used by Alembic.
revision = '0ec384adb82b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'properties',
        Column('id', sa.UUID, primary_key=True),
        Column('bed', sa.SMALLINT, nullable=False),
        Column('bath', sa.FLOAT, nullable=False),
        Column('parking_spots', sa.SMALLINT, nullable=False),
        Column('size', sa.FLOAT, nullable=False),
        Column('price', sa.FLOAT, nullable=False),
        Column('type', sa.VARCHAR, nullable=False),
    )

def downgrade():
    op.drop_table('properties')
