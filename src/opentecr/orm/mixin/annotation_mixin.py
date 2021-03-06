# Copyright (c) 2019, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide a component annotation mixin with the corresponding ORM columns."""


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_mixin, declared_attr, relationship


@declarative_mixin
class AnnotationMixin:
    """
    Define a component annotation mixin.

    Attributes
    ----------
    identifier : str
        The annotation identifier.
    is_deprecated: bool, optional
        Whether the identifier is a deprecated one. Deprecated identifiers are still
        useful for identifying components from old data.
    namespace_id : int
        The foreign key of the related Identifiers.org namespace.

    """

    identifier: str = Column(String, nullable=False, index=True)
    is_deprecated: bool = Column(Boolean, default=False, nullable=False)

    def __init__(self, *, is_deprecated: bool = False, **kwargs) -> None:
        """Create an instance with a default value."""
        super().__init__(**kwargs)
        self.is_deprecated = is_deprecated

    @declared_attr
    def namespace_id(cls):
        """Defer the namespace id field instantiation."""
        return Column(Integer, ForeignKey("namespaces.id"), nullable=False)

    @declared_attr
    def namespace(cls):
        """Defer the namespace field instantiation."""
        return relationship("Namespace")
