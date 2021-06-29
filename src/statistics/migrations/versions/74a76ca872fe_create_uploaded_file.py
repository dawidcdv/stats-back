"""create uploaded file

Revision ID: 74a76ca872fe
Revises: 
Create Date: 2021-04-23 21:44:02.657132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74a76ca872fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'uploaded_file',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('checksum', sa.String(32)),
        sa.Column('size', sa.Integer),
        sa.Column('row', sa.Integer),
        sa.Column('column', sa.Integer),
    )

    op.create_table(
        'statistics',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('file_id', sa.Integer, sa.ForeignKey('uploaded_file.id')),
        sa.Column('name', sa.String(50)),
        sa.Column('description', sa.VARCHAR(2048), nullable=True),
        sa.Column('data_description', sa.JSON(2048)),
    )



def downgrade():
    op.drop_table('uploaded_file')
    op.drop_table('statistics')
