#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import secrets
from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Text, and_
from sqlalchemy.orm import Mapped, mapped_column, relationship

from argilla.server.database import Base

_USER_API_KEY_BYTES_LENGTH = 80


def generate_user_api_key():
    return secrets.token_urlsafe(_USER_API_KEY_BYTES_LENGTH)


def default_inserted_at(context):
    return context.get_current_parameters()["inserted_at"]


class UserRole(str, Enum):
    admin = "admin"
    annotator = "annotator"


class Dataset(Base):
    __tablename__ = "datasets"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str]
    guidelines: Mapped[Optional[str]]
    workspace_id: Mapped[UUID] = mapped_column(ForeignKey("workspaces.id"))

    inserted_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=default_inserted_at, onupdate=datetime.utcnow)

    workspace: Mapped["Workspace"] = relationship(back_populates="datasets")

    def __repr__(self):
        return f"Dataset(id={str(self.id)!r}, name={self.name!r}, guidelines={self.guidelines!r}, inserted_at={str(self.inserted_at)!r}, updated_at={str(self.updated_at)!r})"


class WorkspaceUser(Base):
    __tablename__ = "workspaces_users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    workspace_id: Mapped[UUID] = mapped_column(ForeignKey("workspaces.id"))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

    inserted_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=default_inserted_at, onupdate=datetime.utcnow)

    workspace: Mapped["Workspace"] = relationship(viewonly=True)
    user: Mapped["User"] = relationship(viewonly=True)

    def __repr__(self):
        return f"WorkspaceUser(id={str(self.id)!r}, workspace_id={str(self.workspace_id)!r}, user_id={str(self.user_id)!r}, inserted_at={str(self.inserted_at)!r}, updated_at={str(self.updated_at)!r})"


class Workspace(Base):
    __tablename__ = "workspaces"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True)

    inserted_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=default_inserted_at, onupdate=datetime.utcnow)

    datasets: Mapped[List["Dataset"]] = relationship(back_populates="workspace", order_by=Dataset.inserted_at.asc())
    users: Mapped[List["User"]] = relationship(
        secondary="workspaces_users", back_populates="workspaces", order_by=WorkspaceUser.inserted_at.asc()
    )

    def __repr__(self):
        return f"Workspace(id={str(self.id)!r}, name={self.name!r}, inserted_at={str(self.inserted_at)!r}, updated_at={str(self.updated_at)!r})"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]]
    username: Mapped[str] = mapped_column(unique=True)
    role: Mapped[UserRole] = mapped_column(default=UserRole.annotator)
    api_key: Mapped[str] = mapped_column(Text, unique=True, default=generate_user_api_key)
    password_hash: Mapped[str] = mapped_column(Text)

    inserted_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=default_inserted_at, onupdate=datetime.utcnow)

    workspaces: Mapped[List["Workspace"]] = relationship(
        secondary="workspaces_users", back_populates="users", order_by=WorkspaceUser.inserted_at.asc()
    )
    datasets: Mapped[List["Dataset"]] = relationship(
        secondary="workspaces_users",
        primaryjoin=id == WorkspaceUser.user_id,
        secondaryjoin=and_(
            Workspace.id == Dataset.workspace_id,
            WorkspaceUser.workspace_id == Workspace.id,
        ),
        viewonly=True,
        order_by=Dataset.inserted_at.asc(),
    )

    @property
    def is_admin(self):
        return self.role == UserRole.admin

    @property
    def is_annotator(self):
        return self.role == UserRole.annotator

    def __repr__(self):
        return f"User(id={str(self.id)!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, role={self.role.value!r}, inserted_at={str(self.inserted_at)!r}, updated_at={str(self.updated_at)!r})"