"""
seed initial data into the database

Revision ID: 20231006000000
Revises: 20230331230800
Create Date: 2023-10-06 00:00:00
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

# revision identifiers, used by Alembic.
revision = '20231006000000'
down_revision = '20230331230800'
branch_labels = None
depends_on = None

def upgrade():
    # Insert seed data into the tables
    users_table = table('users',
        column('id', Integer),
        column('username', String),
        column('password', String)
    )

    roles_table = table('roles',
        column('id', Integer),
        column('role_name', String)
    )

    permissions_table = table('permissions',
        column('id', Integer),
        column('permission_name', String)
    )

    # seed data
    op.bulk_insert(users_table,
        [
            {'id': 1, 'username': 'admin', 'password': 'admin_password'},
            {'id': 2, 'username': 'user1', 'password': 'user1_password'},
        ]
    )

    op.bulk_insert(roles_table,
        [
            {'id': 1, 'role_name': 'Admin'},
            {'id': 2, 'role_name': 'User'},
        ]
    )

    op.bulk_insert(permissions_table,
        [
            {'id': 1, 'permission_name': 'Read'},
            {'id': 2, 'permission_name': 'Write'},
        ]
    )

def downgrade():
    op.execute("DELETE FROM users WHERE username IN ('admin', 'user1')")
    op.execute("DELETE FROM roles WHERE role_name IN ('Admin', 'User')")
    op.execute("DELETE FROM permissions WHERE permission_name IN ('Read', 'Write')")
