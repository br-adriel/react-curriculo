"""migration 1

Revision ID: 54164d04fd06
Revises: 
Create Date: 2024-03-31 15:22:39.897963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54164d04fd06'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curriculums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_curriculums_id'), 'curriculums', ['id'], unique=False)
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('curriculum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['curriculum_id'], ['curriculums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_addresses_id'), 'addresses', ['id'], unique=False)
    op.create_table('educations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('degree', sa.String(length=100), nullable=True),
    sa.Column('institution', sa.String(length=100), nullable=True),
    sa.Column('start_date', sa.String(length=10), nullable=True),
    sa.Column('end_date', sa.String(length=10), nullable=True),
    sa.Column('curriculum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['curriculum_id'], ['curriculums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_educations_id'), 'educations', ['id'], unique=False)
    op.create_table('experiences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=100), nullable=True),
    sa.Column('company', sa.String(length=100), nullable=True),
    sa.Column('start_date', sa.String(length=10), nullable=True),
    sa.Column('end_date', sa.String(length=10), nullable=True),
    sa.Column('curriculum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['curriculum_id'], ['curriculums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_experiences_id'), 'experiences', ['id'], unique=False)
    op.create_table('phones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('curriculum_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['curriculum_id'], ['curriculums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_phones_id'), 'phones', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_phones_id'), table_name='phones')
    op.drop_table('phones')
    op.drop_index(op.f('ix_experiences_id'), table_name='experiences')
    op.drop_table('experiences')
    op.drop_index(op.f('ix_educations_id'), table_name='educations')
    op.drop_table('educations')
    op.drop_index(op.f('ix_addresses_id'), table_name='addresses')
    op.drop_table('addresses')
    op.drop_index(op.f('ix_curriculums_id'), table_name='curriculums')
    op.drop_table('curriculums')
    # ### end Alembic commands ###
