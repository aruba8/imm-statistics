"""empty message

Revision ID: 63150775f7
Revises: 525bbe02b2ca
Create Date: 2015-04-15 20:26:49.690365

"""

# revision identifiers, used by Alembic.
revision = '63150775f7'
down_revision = '525bbe02b2ca'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reset',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('uuid', sa.String(length=80), nullable=False),
                    sa.Column('expiration_date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('user_id')
                    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reset')
    ### end Alembic commands ###
