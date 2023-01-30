"""create customers table

Revision ID: f66823dc7132
Revises: 
Create Date: 2023-01-29 23:33:58.448784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f66823dc7132'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customers',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('tax_id', sa.String(length=11), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Customers')
    # ### end Alembic commands ###
