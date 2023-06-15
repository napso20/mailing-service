"""
initial tables creation - create package, post_office and package_status tables

Revision ID: 111111111111

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '111111111111'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'package',
        sa.Column('package_id', sa.VARCHAR(225), nullable=False, primary_key=True),
        sa.Column('destination_address', sa.VARCHAR(512), nullable=False),
        sa.Column('destination_zip_code', sa.VARCHAR(255), nullable=False),
        sa.Column('recipient_name', sa.VARCHAR(255), nullable=True),
        sa.Column('type', sa.VARCHAR(64), nullable=False),
    )

    op.create_table(
        'post_office',
        sa.Column('post_office_id', sa.VARCHAR(225), nullable=False, primary_key=True),
        sa.Column('address', sa.VARCHAR(512), nullable=False),
        sa.Column('zip_code', sa.VARCHAR(255), nullable=True),
        sa.Column('name', sa.VARCHAR(255), nullable=False),
    )

    op.create_table(
        'package_status',
        sa.Column('package_status_id', sa.VARCHAR(225), nullable=False, primary_key=True),
        sa.Column('package_id', sa.VARCHAR(255), nullable=False),
        sa.Column('status', sa.VARCHAR(255), nullable=True),
        sa.Column('timestamp', sa.DateTime()),
        sa.PrimaryKeyConstraint('package_status_id'),
        sa.ForeignKeyConstraint(['package_id'], ['package.package_id'], ondelete='CASCADE')
    )


def downgrade():
    op.drop_table('package_status')
    op.drop_table('post_office')
    op.drop_table('package')
