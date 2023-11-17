"""create_dd_uielement_table

Revision ID: 25c7549f8ada
Revises: d86edbef1d17
Create Date: 2023-11-17 12:21:15.967978

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '25c7549f8ada'
down_revision = 'd86edbef1d17'
branch_labels = None
depends_on = None


def upgrade() -> None:

    enum_values = ['Label', 'Input Field', 'Text Area', 'Checkbox', 'Radio Button', 'Dropdown', 'Date Picker', 'Time Picker', 'File Upload', 'Image', 'Icon', 'Link', 'Tooltip', 'Slider']
    
    op.create_table(
        'dd_uielement',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('EntityID', sa.Integer, nullable=True),
        sa.Column('ElementType', sa.Enum(*enum_values, name='tipodeelemento'), nullable=True),
        sa.Column('ElementName', sa.String(255), nullable=False),
        sa.Column('ElementDescription', sa.Text, nullable=True),
        sa.Column('TypingMask', sa.String(255), nullable=True),
        sa.Column('ValidationRules', sa.Text, nullable=True),
        sa.Column('SystemID', sa.Integer, nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('dd_uielement')
