from svc.models import Session, Package


class PackageDAO:
    def create(self, package):
        with Session() as session:
            session.add(package)
            session.commit()

    def get(self, id):
        with Session() as session:
            return session.query(Package).get(id)
