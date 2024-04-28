"""migration 1

Revision ID: e5dcc35162bf
Revises: 54164d04fd06
Create Date: 2024-03-31 15:50:47.372360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5dcc35162bf'
down_revision: Union[str, None] = '54164d04fd06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_phones_id', table_name='phones')
    op.drop_table('phones')
    op.add_column('curriculums', sa.Column('Phone', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('curriculums', 'Phone')
    op.create_table('phones',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('curriculum_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['curriculum_id'], ['curriculums.id'], name='phones_curriculum_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='phones_pkey')
    )
    op.create_index('ix_phones_id', 'phones', ['id'], unique=False)
    # ### end Alembic commands ###
