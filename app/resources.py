import geopy.distance
from flask import request, jsonify
from flask_restful import Resource, abort

from app.models import CommunityModel, EnrollmentModel

DER_THRESHOLD = 0.5


class Community(Resource):

    def get(self, community_name):
        comm = CommunityModel.objects.get_or_404(name=community_name)
        return jsonify(comm)

    def post(self):
        args = request.get_json()

        comm = CommunityModel(
            name=args['name'],
            description=args['description'],
            manager_id=args['manager_id'],
            position=args['position'])
        comm.save()
        return comm.to_json(), 201

    def put(self, community_name):
        comm = CommunityModel.objects.get_or_404(name=community_name)

        args = request.get_json()
        comm.description = str(args['description'])
        comm.manager_id = str(args['manager_id'])
        comm.position = args['position']
        comm.save()
        return comm.to_json(), 200

    def delete(self, community_name):
        comm = CommunityModel.objects.get_or_404(name=community_name)
        comm.delete()
        return '', 200


def is_close_to_comm(point1, point2):
    return geopy.distance.vincenty(point1.values(), point2.values()).km < DER_THRESHOLD


class CommunityEnrollment(Resource):

    def post(self, community_name):
        # get community
        comm = CommunityModel.objects.get_or_404(name=community_name)
        args = request.get_json()
        is_close_to_comm(args['der']['position'], comm.position) or abort(
            400,
            message="DER must be closer to the community")
        enrollment = EnrollmentModel(
            member_id=args['member_id'],
            name=args['name'],
            surname=args.get('surname'),
            der=args['der'],
        )
        enrollment.save()
        return enrollment.to_json(), 201
