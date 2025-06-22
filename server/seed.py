from server import create_app, db
from server.models import Guest, Episode, Appearance

app = create_app()
app.app_context().push()

# Sample data
guests = [
    Guest(name="John Doe", occupation="Comedian"),
    Guest(name="Jane Smith", occupation="Musician"),
    Guest(name="Mike Johnson", occupation="Actor")
]

episodes = [
    Episode(date="2023-01-01", number=101),
    Episode(date="2023-01-08", number=102)
]

appearances = [
    Appearance(rating=4, guest=guests[0], episode=episodes[0]),
    Appearance(rating=5, guest=guests[1], episode=episodes[0]),
    Appearance(rating=3, guest=guests[2], episode=episodes[1])
]

# Add to session and commit
with app.app_context():
    db.session.add_all(guests)
    db.session.add_all(episodes)
    db.session.commit()
    
    db.session.add_all(appearances)
    db.session.commit()

print("Database seeded successfully!")