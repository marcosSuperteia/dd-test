"""create_dd_attribute_table

Revision ID: ac332c906e54
Revises: b2a1c38cc6f9
Create Date: 2023-11-13 18:30:00.266385

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'ac332c906e54'
down_revision = 'b2a1c38cc6f9'
branch_labels = None
depends_on = None


def upgrade() -> None:

        enum_values = ['Integer', 'Float', 'String', 'Date', 'Time', 'DateTime', 'Boolean', 'Currency', 'Email', 'URL', 'Phone Number', 'Address', 'Image', 'File', 'Password']

        op.create_table(
        'dd_attribute',
        sa.Column('id', sa.Integer, nullable=False, autoincrement=True),
        sa.Column('EntityID', sa.Integer, nullable=True),
        sa.Column('AttributeName', sa.String(255), nullable=False),
        sa.Column('DataType', sa.Enum(*enum_values, name='tipodedado'), nullable=True),
        sa.Column('size', sa.DECIMAL(7, 0), nullable=True, server_default='0', comment='Tamanho do Atributo'),
        sa.Column('label', sa.String(100), nullable=True, comment='Label que será utilizado na montagem das Telas.\r\nCaso omitido o nome do Atributo será utilizado.'),
        sa.Column('tooltip', sa.String(250), nullable=True, comment='Texto sintético a ser utilizado no preenchimento automático do Tooltip quando o usuário estiver com o Mouse sobre o campo.'),
        sa.Column('help', sa.Text, nullable=True, comment='Texto / HTML descritivo - que será utilizado para montagem do HELP do Sistema'),
        sa.Column('IsRequired', sa.Boolean, nullable=True, comment='Indica se o atributo é obrigatório'),
        sa.Column('DefaultValue', sa.Text, nullable=True, comment='Armazena o valor padrão do atributo'),
        sa.Column('ValidationRules', sa.Text, nullable=True, comment='Especifica regras de validação personalizadas para o atributo'),
        sa.Column('IsIndexed', sa.Boolean, nullable=True, comment='Indica se o atributo é indexado para consultas mais rápidas'),
        sa.Column('IsUnique', sa.Boolean, nullable=True, comment='Indica se os valores do atributo devem ser únicos'),
        sa.Column('MinimumValue', sa.DECIMAL(18, 6), nullable=True, comment='Especifica o valor mínimo para o atributo'),
        sa.Column('MaximumValue', sa.DECIMAL(18, 6), nullable=True, comment='Especifica o valor máximo para o atributo'),
        sa.Column('ForeignKeyEntity', sa.Integer, nullable=True, comment='Referencia entidades relacionadas (se o atributo for uma chave estrangeira)'),
        sa.Column('IsHidden', sa.Boolean, nullable=True, comment='Indica se o atributo deve ser oculto na interface do usuário'),
        # sa.Column('IsReadOnly', sa.Boolean, nullable=True, comment='Indica se o atributo é somente leitura'),
        # sa.Column('IsSystem', sa.Boolean, nullable=True, comment='Indica se o atributo é um atributo de sistema'),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('dd_attribute')
