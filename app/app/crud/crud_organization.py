from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate


class CRUDOrganization(CRUDBase[Organization, OrganizationCreate, OrganizationUpdate]):
    def get_all_organizations(self, db: Session) -> List[Organization]:
        return db.query(self.model).all()


organization = CRUDOrganization(Organization)
