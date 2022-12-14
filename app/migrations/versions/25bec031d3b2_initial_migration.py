"""Initial migration

Revision ID: 25bec031d3b2
Revises: 
Create Date: 2022-12-11 20:17:32.209368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25bec031d3b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category_table',
    sa.Column('id', sa.Integer(), sa.Identity(always=True), autoincrement=True, nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_category_table_id'), 'category_table', ['id'], unique=False)
    op.create_table('product_table',
    sa.Column('id', sa.Integer(), sa.Identity(always=True), autoincrement=True, nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_table_id'), 'product_table', ['id'], unique=False)
    op.create_table('product_category',
    sa.Column('product_pk', sa.Integer(), nullable=False),
    sa.Column('category_pk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_pk'], ['category_table.id'], ),
    sa.ForeignKeyConstraint(['product_pk'], ['product_table.id'], ),
    sa.PrimaryKeyConstraint('product_pk', 'category_pk')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_category')
    op.drop_index(op.f('ix_product_table_id'), table_name='product_table')
    op.drop_table('product_table')
    op.drop_index(op.f('ix_category_table_id'), table_name='category_table')
    op.drop_table('category_table')
    # ### end Alembic commands ###
