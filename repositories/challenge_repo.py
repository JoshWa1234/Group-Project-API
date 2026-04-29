from sqlalchemy.orm import Session
from models.challenge_model import Challenge
from schema.challenge_schema import ChallengeCreateRequest


class ChallengeRepository:
    def create_challenge(self, db: Session, challenge: ChallengeCreateRequest):
        db_challenge = Challenge(
            title=challenge.title,
            description=challenge.description,
            points=challenge.points,
            target=challenge.target,
            frequency=challenge.frequency,
            due_date=challenge.due_date,
            assigned_to=challenge.assigned_to,
            status="In Progress"
            )

        db.add(db_challenge)
        db.commit()
        db.refresh(db_challenge)

        return db_challenge
    
    def update_progress(self, db: Session, challenge_id: int, progress: int):
        challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()

        if not challenge:
            return None

        challenge.progress = progress

        if challenge.progress >= challenge.target:
            challenge.progress = challenge.target
            challenge.status = "Completed"

        db.commit()
        db.refresh(challenge)

        return challenge

    def get_all_challenges(self, db: Session):
        return db.query(Challenge).all()

    def get_in_progress_challenges(self, db: Session):
        return db.query(Challenge).filter(Challenge.status == "In Progress").all()
    
    def retire_challenge(self, db: Session, challenge_id: int):
        challenge = db.query(Challenge).filter(Challenge.id == challenge_id).first()

        if not challenge:
            return None

        challenge.status = "Cancelled by Challenge Master"

        db.commit()
        db.refresh(challenge)

        return challenge
    
    def get_history_challenges(self, db: Session):
        return db.query(Challenge).filter(Challenge.status != "In Progress").all()
    
    def get_challenge_by_id(self, id: int, db: Session):
        return db.query(Challenge).filter(Challenge.id == id).first()