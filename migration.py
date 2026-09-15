from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create Users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False, unique=True),
        sa.Column('password', sa.String(length=50), nullable=False)
    )

    # Create Roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role_name', sa.String(length=50), nullable=False, unique=True)
    )

    # Create Permissions table
    op.create_table(
        'permissions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('permission_name', sa.String(length=50), nullable=False, unique=True)
    )

    # Create Audit table
    op.create_table(
        'audit',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('action', sa.String(length=255))
    )

def downgrade():
    # Drop tables on downgrades
    op.drop_table('audit')
    op.drop_table('permissions')
    op.drop_table('roles')
    op.drop_table('users')