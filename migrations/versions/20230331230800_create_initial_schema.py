"""Create initial database schema

Revision ID: 20230331230800
Revises: 
Create Date: 2023-03-31 23:08:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20230331230800'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Ensure tables are created correctly
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(length=50), unique=True),
        sa.Column('password', sa.String(length=50))
    )
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role_name', sa.String(length=50), unique=True)
    )
    op.create_table(
        'permissions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('permission_name', sa.String(length=50), unique=True)
    )
    op.create_table(
        'audit',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('action', sa.String(length=255))
    )

    # Create tables
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(length=50), unique=True),
        sa.Column('password', sa.String(length=50))
    )
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role_name', sa.String(length=50), unique=True)
    )
    op.create_table(
        'permissions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('permission_name', sa.String(length=50), unique=True)
    )
    op.create_table(
        'audit',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('action', sa.String(length=255))
    )

def downgrade():
    # Drop tables
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('permissions')
    op.drop_table('audit')
