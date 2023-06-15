from svc.models import Session, PostOffice


class PostOfficeDAO:
    def create(self, post_office):
        with Session() as session:
            session.add(post_office)
            session.commit()

    def get(self, post_office_id):
        with Session() as session:
            return session.query(PostOffice).get(post_office_id)
