"""create_dd_businessrule_table

Revision ID: bf6e25960cf2
Revises: ac332c906e54
Create Date: 2023-11-16 11:55:13.905424

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bf6e25960cf2'
down_revision = 'ac332c906e54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dd_businessrule',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('EntityID', sa.Integer),
        sa.Column('RuleName', sa.String(255), nullable=False),
        sa.Column('RuleDescription', sa.Text),
        sa.Column('SystemID', sa.Integer),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )

def downgrade() -> None:
    op.drop_table('dd_businessrule')