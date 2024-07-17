from typing import List

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db


class _Rename_This_Model_(db.Model):
    __tablename__ = "table"

    id: Mapped[int] = mapped_column(primary_key=True)
    