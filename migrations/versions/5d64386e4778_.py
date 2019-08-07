"""empty message

Revision ID: 5d64386e4778
Revises: 60486c13ab73
Create Date: 2019-08-07 01:43:42.509264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d64386e4778'
down_revision = '60486c13ab73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_abstracts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('abstract', sa.String(length=1000), nullable=False),
    sa.Column('added_on', sa.DateTime(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_abstracts')
    # ### end Alembic commands ###
