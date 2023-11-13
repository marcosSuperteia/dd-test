"""create_dd_systems_table

Revision ID: 0a2596d5b243
Revises: 6d5ebb85f6c1
Create Date: 2023-11-13 13:29:30.733779

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '0a2596d5b243'
down_revision = '6d5ebb85f6c1'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table(
            "dd_system",
            sa.Column("id", sa.Integer(), nullable=False, autoincrement=True),
            sa.Column("SystemName", sa.String(length=255), nullable=False),
            sa.Column("SystemPrefix", sa.String(length=3), nullable=True, comment="Prefixo com até 3 letras que será adicionado na criação das tabelas deste sistema."),
            sa.Column("Description", sa.Text(), nullable=True),
            sa.Column("CustomerID", sa.Integer(), nullable=True),
            sa.Column("data_entry_order", sa.Text(), nullable=False, comment="DATA Entry order to ensure that the data modeling and structure will succeed, aligning the functionalities and interactions needed for the system."),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.Column("updated_at", sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint("id")
        )



def downgrade() -> None:
    op.drop_table("dd_system")
