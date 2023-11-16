"""create_dd_relationship_table

Revision ID: d86edbef1d17
Revises: 8bd7147286c0
Create Date: 2023-11-16 12:43:14.781999

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd86edbef1d17'
down_revision = '8bd7147286c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dd_relationship',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('ParentEntityID', sa.Integer),
        sa.Column('ChildEntityID', sa.Integer),
        sa.Column('Description', sa.Text),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('dd_relationship')
    
