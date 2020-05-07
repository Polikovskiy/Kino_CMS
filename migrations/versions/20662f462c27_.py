"""empty message

Revision ID: 20662f462c27
Revises: 
Create Date: 2020-05-05 17:03:22.670277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20662f462c27'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('film',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('image', sa.String(length=500), nullable=True),
    sa.Column('description', sa.String(length=10000), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('trailer', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('CEO__blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=500), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('keywords', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=10000), nullable=True),
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('galery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=500), nullable=True),
    sa.Column('film_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['film_id'], ['film.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('galery')
    op.drop_table('CEO__blog')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('film')
    # ### end Alembic commands ###
