from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create Password History table
    op.create_table(
        'password_history',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False)
    )
    # Create Login Attempts table
    op.create_table(
        'login_attempts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('timestamp', sa.DateTime, nullable=False),
        sa.Column('success', sa.Boolean, nullable=False)
    )
    # Creating Users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False, unique=True),
        sa.Column('password', sa.String(length=50), nullable=False)
    )
    # Creating Roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role_name', sa.String(length=50), nullable=False, unique=True)
    )
    # Creating Permissions table
    op.create_table(
        'permissions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('permission_name', sa.String(length=50), nullable=False, unique=True)
    )
    # Creating Audit table
    op.create_table(
        'audit',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('action', sa.String(length=255))
    )
    # Create Password History table
    op.create_table(
        'password_history',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False)
    )
    # Create Login Attempts table
    op.create_table(
        'login_attempts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('timestamp', sa.DateTime, nullable=False),
        sa.Column('success', sa.Boolean, nullable=False)
    )
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
    # Dropping tables if they exist
    op.drop_table('audit')
    op.drop_table('permissions')
    op.drop_table('roles')
    op.drop_table('users')
    op.drop_table('login_attempts')
    op.drop_table('password_history')

    # Drop tables on downgrades
    op.drop_table('audit')
    op.drop_table('permissions')
    op.drop_table('roles')
    op.drop_table('users')