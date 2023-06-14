from svc.models.dao.post_office_dao import PostOfficeDAO
from svc.models.dao.package_dao import PackageDAO


class MailService:
    def __init__(self):
        self.post_office_dao = PostOfficeDAO()
        self.package_dao = PackageDAO()

    def register_post_office(self, post_office):
        return self.post_office_dao.create(post_office)

    def get_post_office(self, id):
        return self.post_office_dao.get_by_id(id)

    def register_package(self, package):
        return self.package_dao.create(package)

    def get_package_status_history(self, id):
        return self.package_dao.get_status_history(id)

    def record_arrival(self, post_office_id, package_id):
        post_office = self.post_office_dao.get(post_office_id)
        if not post_office:
            return None
        return self.package_dao.record_arrival(post_office_id, package_id)

    def record_departure(self, post_office_id, package_id):
        post_office = self.post_office_dao.get(post_office_id)
        if not post_office:
            return None
        return self.package_dao.record_departure(post_office_id, package_id)
