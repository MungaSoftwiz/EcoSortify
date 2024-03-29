"""initial migration

Revision ID: 2fa4841e4f36
Revises:
Create Date: 2024-03-16 19:04:51.640483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fa4841e4f36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('posts')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index('ix_users_email')
        batch_op.drop_index('ix_users_username')

    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('email', sa.VARCHAR(length=64), nullable=True),
                    sa.Column('username', sa.VARCHAR(length=64),
                              nullable=True),
                    sa.Column('password_hash', sa.VARCHAR(length=128),
                              nullable=True),
                    sa.Column('created_at', sa.DATETIME(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index('ix_users_username', ['username'], unique=1)
        batch_op.create_index('ix_users_email', ['email'], unique=1)

    op.create_table('posts',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('author_id', sa.INTEGER(), nullable=True),
                    sa.Column('title', sa.VARCHAR(length=64), nullable=True),
                    sa.Column('content', sa.TEXT(), nullable=True),
                    sa.Column('created_at', sa.DATETIME(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('comments',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('author_id', sa.INTEGER(), nullable=True),
                    sa.Column('post_id', sa.INTEGER(), nullable=True),
                    sa.Column('content', sa.TEXT(), nullable=True),
                    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###
