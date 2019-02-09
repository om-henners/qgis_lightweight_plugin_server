"""Change plugin to plugin_id

Revision ID: 14c29f811e9f
Revises: cf73efec70c9
Create Date: 2019-02-09 23:33:48.934369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14c29f811e9f'
down_revision = 'cf73efec70c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plugin_version', sa.Column('plugin_id', sa.Integer(), nullable=False))
    op.drop_constraint('plugin_version_plugin_fkey', 'plugin_version', type_='foreignkey')
    op.create_foreign_key(None, 'plugin_version', 'plugin', ['plugin_id'], ['id'])
    op.drop_column('plugin_version', 'plugin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plugin_version', sa.Column('plugin', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'plugin_version', type_='foreignkey')
    op.create_foreign_key('plugin_version_plugin_fkey', 'plugin_version', 'plugin', ['plugin'], ['id'])
    op.drop_column('plugin_version', 'plugin_id')
    # ### end Alembic commands ###