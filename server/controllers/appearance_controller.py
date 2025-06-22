from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.episode import Episode
from server.models.guest import Guest
from server.extensions import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    # Validate data
    if not all(key in data for key in ['rating', 'guest_id', 'episode_id']):
        return jsonify({"message": "Missing required fields"}), 400
    
    if not (1 <= data['rating'] <= 5):
        return jsonify({"message": "Rating must be between 1 and 5"}), 400
    
    # Check if guest and episode exist
    guest = Guest.query.get(data['guest_id'])
    if not guest:
        return jsonify({"message": "Guest not found"}), 404
    
    episode = Episode.query.get(data['episode_id'])
    if not episode:
        return jsonify({"message": "Episode not found"}), 404
    
    # Create appearance
    appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201