from flask import Flask, jsonify, request
from svc.models import Package, PostOffice, PackageStatus
from svc.models.dao.package_dao import PackageDAO
from svc.models.dao.post_office_dao import PostOfficeDAO
from svc.models.dao.package_status_dao import PackageStatusDAO

app = Flask(__name__)
package_dao = PackageDAO()
post_office_dao = PostOfficeDAO()
package_status_dao = PackageStatusDAO()


@app.route('/postoffice', methods=['POST'])
def register_post_office():
    try:
        data = request.get_json()
        post_office = PostOffice(**data)
        post_office_dao.create(post_office)
        return jsonify(message='Post office registered successfully'), 200
    except Exception as e:
        return jsonify(message='Error registering post office', error=str(e)), 500


@app.route('/postoffice/<int:id>', methods=['GET'])
def get_post_office(id):
    try:
        post_office = post_office_dao.get(id)
        if post_office:
            return jsonify(post_office), 200
        else:
            return jsonify(message='Post office not found'), 404
    except Exception as e:
        return jsonify(message='Error retrieving post office', error=str(e)), 500


@app.route('/package', methods=['POST'])
def register_package():
    try:
        data = request.get_json()
        package = Package(**data)
        package_dao.create(package)
        return jsonify(message='Package registered successfully'), 200
    except Exception as e:
        return jsonify(message='Error registering package', error=str(e)), 500


@app.route('/package/<int:id>', methods=['GET'])
def get_package_status_history(id):
    try:
        package = package_dao.get(id)
        if package:
            status_history = package_status_dao.get_status_history(id)
            return jsonify({'id': package.id, 'history': status_history}), 200
        else:
            return jsonify(message='Package not found'), 404
    except Exception as e:
        return jsonify(message='Error retrieving package status history', error=str(e)), 500


@app.route('/postoffice/<int:id>/arrival', methods=['POST'])
def record_arrival(id):
    try:
        data = request.get_json()
        package_id = data.get('package_id')
        package = package_dao.get(package_id)
        if package:
            status = f"Arrived at post office {id}"
            package.add_status(status)
            package_status = PackageStatus(package_id=package_id, status=status)
            package_status_dao.create(package_status)
            return jsonify(message='Arrival recorded successfully'), 200
        else:
            return jsonify(message='Package not found'), 404
    except Exception as e:
        return jsonify(message='Error recording arrival', error=str(e)), 500


@app.route('/postoffice/<int:id>/departure', methods=['POST'])
def record_departure(id):
    try:
        data = request.get_json()
        package_id = data.get('package_id')
        package = package_dao.get(package_id)
        if package:
            status = f"Departed from post office {id}"
            package.add_status(status)
            package_status = PackageStatus(package_id=package_id, status=status)
            package_status_dao.create(package_status)
            return jsonify(message='Departure recorded successfully'), 200
        else:
            return jsonify(message='Package not found'), 404
    except Exception as e:
        return jsonify(message='Error recording departure', error=str(e)), 500
