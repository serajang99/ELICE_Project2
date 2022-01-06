"""genre_matrix

Revision ID: 5a95614f9a40
Revises: ca4ece03dd78
Create Date: 2021-12-30 07:31:56.528915

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from seed.datatread import matrix_maker


# revision identifiers, used by Alembic.
revision = '5a95614f9a40'
down_revision = 'ca4ece03dd78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Genre_Matrix',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('top1', sa.Integer(), nullable=False),
    sa.Column('top2', sa.Integer(), nullable=False),
    sa.Column('top3', sa.Integer(), nullable=False),
    sa.Column('top4', sa.Integer(), nullable=False),
    sa.Column('top5', sa.Integer(), nullable=False),
    sa.Column('top6', sa.Integer(), nullable=False),
    sa.Column('top7', sa.Integer(), nullable=False),
    sa.Column('top8', sa.Integer(), nullable=False),
    sa.Column('top9', sa.Integer(), nullable=False),
    sa.Column('top10', sa.Integer(), nullable=False),
    sa.Column('top11', sa.Integer(), nullable=False),
    sa.Column('top12', sa.Integer(), nullable=False),
    sa.Column('top13', sa.Integer(), nullable=False),
    sa.Column('top14', sa.Integer(), nullable=False),
    sa.Column('top15', sa.Integer(), nullable=False),
    sa.Column('top16', sa.Integer(), nullable=False),
    sa.Column('top17', sa.Integer(), nullable=False),
    sa.Column('top18', sa.Integer(), nullable=False),
    sa.Column('top19', sa.Integer(), nullable=False),
    sa.Column('top20', sa.Integer(), nullable=False),
    sa.Column('top21', sa.Integer(), nullable=False),
    sa.Column('top22', sa.Integer(), nullable=False),
    sa.Column('top23', sa.Integer(), nullable=False),
    sa.Column('top24', sa.Integer(), nullable=False),
    sa.Column('top25', sa.Integer(), nullable=False),
    sa.Column('top26', sa.Integer(), nullable=False),
    sa.Column('top27', sa.Integer(), nullable=False),
    sa.Column('top28', sa.Integer(), nullable=False),
    sa.Column('top29', sa.Integer(), nullable=False),
    sa.Column('top30', sa.Integer(), nullable=False),
    sa.Column('top31', sa.Integer(), nullable=False),
    sa.Column('top32', sa.Integer(), nullable=False),
    sa.Column('top33', sa.Integer(), nullable=False),
    sa.Column('top34', sa.Integer(), nullable=False),
    sa.Column('top35', sa.Integer(), nullable=False),
    sa.Column('top36', sa.Integer(), nullable=False),
    sa.Column('top37', sa.Integer(), nullable=False),
    sa.Column('top38', sa.Integer(), nullable=False),
    sa.Column('top39', sa.Integer(), nullable=False),
    sa.Column('top40', sa.Integer(), nullable=False),
    sa.Column('top41', sa.Integer(), nullable=False),
    sa.Column('top42', sa.Integer(), nullable=False),
    sa.Column('top43', sa.Integer(), nullable=False),
    sa.Column('top44', sa.Integer(), nullable=False),
    sa.Column('top45', sa.Integer(), nullable=False),
    sa.Column('top46', sa.Integer(), nullable=False),
    sa.Column('top47', sa.Integer(), nullable=False),
    sa.Column('top48', sa.Integer(), nullable=False),
    sa.Column('top49', sa.Integer(), nullable=False),
    sa.Column('top50', sa.Integer(), nullable=False),
    sa.Column('top51', sa.Integer(), nullable=False),
    sa.Column('top52', sa.Integer(), nullable=False),
    sa.Column('top53', sa.Integer(), nullable=False),
    sa.Column('top54', sa.Integer(), nullable=False),
    sa.Column('top55', sa.Integer(), nullable=False),
    sa.Column('top56', sa.Integer(), nullable=False),
    sa.Column('top57', sa.Integer(), nullable=False),
    sa.Column('top58', sa.Integer(), nullable=False),
    sa.Column('top59', sa.Integer(), nullable=False),
    sa.Column('top60', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['Contents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    
    matrix = matrix_maker()
    
    seed_matrix_table = table('Genre_Matrix',
        column('id', sa.Integer),
        column('top1', sa.Integer()),
        column('top2', sa.Integer()),
        column('top3', sa.Integer()),
        column('top4', sa.Integer()),
        column('top5', sa.Integer()),
        column('top6', sa.Integer()),
        column('top7', sa.Integer()),
        column('top8', sa.Integer()),
        column('top9', sa.Integer()),
        column('top10', sa.Integer()),
        column('top11', sa.Integer()),
        column('top12', sa.Integer()),
        column('top13', sa.Integer()),
        column('top14', sa.Integer()),
        column('top15', sa.Integer()),
        column('top16', sa.Integer()),
        column('top17', sa.Integer()),
        column('top18', sa.Integer()),
        column('top19', sa.Integer()),
        column('top20', sa.Integer()),
        column('top21', sa.Integer()),
        column('top22', sa.Integer()),
        column('top23', sa.Integer()),
        column('top24', sa.Integer()),
        column('top25', sa.Integer()),
        column('top26', sa.Integer()),
        column('top27', sa.Integer()),
        column('top28', sa.Integer()),
        column('top29', sa.Integer()),
        column('top30', sa.Integer()),
        column('top31', sa.Integer()),
        column('top32', sa.Integer()),
        column('top33', sa.Integer()),
        column('top34', sa.Integer()),
        column('top35', sa.Integer()),
        column('top36', sa.Integer()),
        column('top37', sa.Integer()),
        column('top38', sa.Integer()),
        column('top39', sa.Integer()),
        column('top40', sa.Integer()),
        column('top41', sa.Integer()),
        column('top42', sa.Integer()),
        column('top43', sa.Integer()),
        column('top44', sa.Integer()),
        column('top45', sa.Integer()),
        column('top46', sa.Integer()),
        column('top47', sa.Integer()),
        column('top48', sa.Integer()),
        column('top49', sa.Integer()),
        column('top50', sa.Integer()),
        column('top51', sa.Integer()),
        column('top52', sa.Integer()),
        column('top53', sa.Integer()),
        column('top54', sa.Integer()),
        column('top55', sa.Integer()),
        column('top56', sa.Integer()),
        column('top57', sa.Integer()),
        column('top58', sa.Integer()),
        column('top59', sa.Integer()),
        column('top60', sa.Integer()),
    )
    op.bulk_insert(seed_matrix_table, matrix)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Genre_Matrix')
    # ### end Alembic commands ###
