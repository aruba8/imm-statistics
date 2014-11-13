"""empty message

Revision ID: 312ddd5e5bb7
Revises: None
Create Date: 2014-11-12 20:58:17.380669

"""

# revision identifiers, used by Alembic.
revision = '312ddd5e5bb7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('user_dataDB',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('stream', sa.String(collation='NOCASE'), nullable=True),
    sa.Column('from_short', sa.String(), nullable=True),
    sa.Column('from_full', sa.String(), nullable=True),
    sa.Column('interview_location', sa.String(collation='NOCASE'), nullable=True),
    sa.Column('interview_date', sa.DateTime(), nullable=True),
    sa.Column('invitation_to_apply_date', sa.DateTime(), nullable=True),
    sa.Column('mpnp_file_date', sa.DateTime(), nullable=True),
    sa.Column('mpnp_request_additional_docs_date', sa.DateTime(), nullable=True),
    sa.Column('mpnp_nomination_date', sa.DateTime(), nullable=True),
    sa.Column('cio_received_date', sa.DateTime(), nullable=True),
    sa.Column('cio_processing_fee_date', sa.DateTime(), nullable=True),
    sa.Column('cio_file_number', sa.DateTime(), nullable=True),
    sa.Column('embassy', sa.String(collation='NOCASE'), nullable=True),
    sa.Column('ecas_recieved', sa.DateTime(), nullable=True),
    sa.Column('ecas_in_process', sa.DateTime(), nullable=True),
    sa.Column('ecas_additional_documents_request1', sa.DateTime(), nullable=True),
    sa.Column('ecas_medical_forms', sa.DateTime(), nullable=True),
    sa.Column('ecas_medical_exam_passed', sa.DateTime(), nullable=True),
    sa.Column('ecas_medical_results_received', sa.DateTime(), nullable=True),
    sa.Column('ecas_additional_documents_request2', sa.DateTime(), nullable=True),
    sa.Column('povl_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_dataDB')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_table('session')
    ### end Alembic commands ###