from flask import Blueprint, jsonify
from datetime import datetime, timedelta
import random

api_bp = Blueprint('api', __name__)

# Generate 50 sample episodes
def generate_episodes():
    episodes = []
    start_date = datetime(2023, 1, 1)
    guest_pool = [
        "John Mulaney", "Taylor Swift", "Dave Chappelle", 
        "Emma Stone", "The Weeknd", "Ali Wong",
        "Tom Hanks", "Beyoncé", "Kevin Hart", "Lady Gaga"
    ]
    
    for i in range(1, 51):
        episode_date = start_date + timedelta(days=7*i)
        num_guests = random.randint(1, 4)
        
        episodes.append({
            "id": i,
            "date": episode_date.strftime("%Y-%m-%d"),
            "number": 100 + i,
            "title": f"Episode {i}",
            "description": f"Show #{i} with amazing performances",
            "guests": random.sample(guest_pool, num_guests),
            "viewers": f"{random.randint(1, 5)}.{random.randint(0, 9)} million",
            "rating": round(random.uniform(3.5, 5.0), 1)
        })
    
    return episodes

# Pre-generate the episodes data
sample_episodes = generate_episodes()

@api_bp.route('/episodes', methods=['GET'])
def get_episodes():
    return jsonify({
        "status": "success",
        "count": len(sample_episodes),
        "data": sample_episodes
    })

@api_bp.route('/episodes/<int:episode_id>', methods=['GET'])
def get_episode(episode_id):
    episode = next((e for e in sample_episodes if e['id'] == episode_id), None)
    if episode:
        return jsonify(episode)
    return jsonify({"error": "Episode not found"}), 404

@api_bp.route('/episodes/random', methods=['GET'])
def random_episode():
    return jsonify(random.choice(sample_episodes))
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/test', methods=['GET'])
def test_route():
    return jsonify({
        "status": "success",
        "message": "API is working!",
        "endpoints": [
            "/api/test",
            "/api/episodes",
            "/api/episodes/<id>"
        ]
    })

@api_bp.route('/episodes', methods=['GET'])
def get_episodes():
    return jsonify({
        "data": [
            {
                "id": 1,
                "title": "Sample Episode",
                "date": "2023-01-01"
            }
        ]
    })

@api_bp.route('/<path:undefined>')
def catch_all(undefined):
    return jsonify({
        "error": "Route not found",
        "available_routes": [
            "/api/test",
            "/api/episodes"
        ]
    }), 404
@api_bp.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Late Show API",
        "endpoints": {
            "test": "/api/test",
            "episodes": "/api/episodes",
            "random_episode": "/api/episodes/random"
        }
    })