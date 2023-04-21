"""create measurments table

Revision ID: b96d2a446f8e
Revises: 
Create Date: 2023-04-21 02:27:25.479794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b96d2a446f8e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "measurments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("height_cm", sa.Float),
        sa.Column("weight_kg", sa.Float),
        sa.Column("age", sa.Float),
        sa.Column("waist_cm", sa.Float),
        
    )


def downgrade() -> None:
    op.drop_table("measurments")
