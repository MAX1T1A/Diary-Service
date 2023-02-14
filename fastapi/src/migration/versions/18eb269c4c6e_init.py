"""init

Revision ID: 18eb269c4c6e
Revises: 
Create Date: 2023-02-09 12:09:37.431307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18eb269c4c6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=120), nullable=False),
                    sa.Column('name', sa.String(length=120), nullable=False),
                    sa.Column('password', sa.String(length=120), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.create_table('diary',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=120), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_diary_user_id'), 'diary', ['user_id'], unique=False)
    op.create_table('page',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=120), nullable=True),
                    sa.Column('body', sa.Text(), nullable=True),
                    sa.Column('diary_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['diary_id'], ['diary.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_page_diary_id'), 'page', ['diary_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_page_diary_id'), table_name='page')
    op.drop_table('page')
    op.drop_index(op.f('ix_diary_user_id'), table_name='diary')
    op.drop_table('diary')
    op.drop_table('user')
    # ### end Alembic commands ###
