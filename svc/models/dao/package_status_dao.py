from svc.models import Session, PackageStatus


class PackageStatusDAO:
    def create(self, package_status):
        with Session() as session:
            session.add(package_status)
            session.commit()

    def get_status_history(self, package_id):
        with Session() as session:
            return session.query(PackageStatus).filter_by(package_id=package_id).all()
