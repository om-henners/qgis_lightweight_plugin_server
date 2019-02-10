"""Enable postgis

Revision ID: aba122a67747
Revises: 14c29f811e9f
Create Date: 2019-02-10 13:37:05.967568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aba122a67747'
down_revision = '14c29f811e9f'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('create extension if not exists postgis')


def downgrade():
    op.execute('drop extension postgis')
