"""initial tables creation - create package, post_office and package_status tables

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
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('destination_address', sa.String(), nullable=False),
        sa.Column('recipient_name', sa.String(), nullable=False),
        sa.Column('type', sa.String(), nullable=False),
    )

    op.create_table(
        'post_office',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('zip_code', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False)
    )

    op.create_table(
        'package_status',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('package_id', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False),  # Add timestamp column
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['package_id'], ['package.id'], ondelete='CASCADE')
    )


def downgrade():
    op.drop_table('package_status')
    op.drop_table('post_office')
    op.drop_table('package')
