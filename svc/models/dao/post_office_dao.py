from svc.models import Session, PostOffice


class PostOfficeDAO:
    def create(self, post_office):
        with Session() as session:
            session.add(post_office)
            session.commit()

    def get(self, id):
        with Session() as session:
            return session.query(PostOffice).get(id)
