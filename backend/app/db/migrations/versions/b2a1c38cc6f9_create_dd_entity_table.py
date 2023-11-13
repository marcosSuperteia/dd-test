"""create_dd_entity_table

Revision ID: b2a1c38cc6f9
Revises: 0a2596d5b243
Create Date: 2023-11-13 17:00:54.673511

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'b2a1c38cc6f9'
down_revision = '0a2596d5b243'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dd_entity',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('EntityName', sa.String(255), nullable=False),
        sa.Column('Description', sa.Text, nullable=True),
        sa.Column('SystemID', sa.Integer, nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )

def downgrade() -> None:
    op.drop_table('dd_entity')