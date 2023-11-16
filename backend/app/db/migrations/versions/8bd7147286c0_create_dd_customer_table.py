"""create_dd_customer_table

Revision ID: 8bd7147286c0
Revises: bf6e25960cf2
Create Date: 2023-11-16 12:14:32.254147

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8bd7147286c0'
down_revision = 'bf6e25960cf2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dd_customer',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('CustomerName', sa.String(255), nullable=False),
        sa.Column('Description', sa.Text),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('dd_customer')
