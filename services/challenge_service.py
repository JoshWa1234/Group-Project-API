from sqlalchemy.orm import Session
from repositories.challenge_repo import ChallengeRepository
from schema.challenge_schema import ChallengeCreateRequest
from fastapi import HTTPException


class ChallengeService:
    def __init__(self):
        self.repo = ChallengeRepository()

    def create_challenge(self, db: Session, challenge: ChallengeCreateRequest):
        return self.repo.create_challenge(db, challenge)

    def get_all_challenges(self, db: Session):
        return self.repo.get_all_challenges(db)

    def get_in_progress_challenges(self, db: Session):
        return self.repo.get_in_progress_challenges(db)
    
    def retire_challenge(self, db: Session, challenge_id: int):
        return self.repo.retire_challenge(db, challenge_id)
    
    def get_history_challenges(self, db: Session):
        return self.repo.get_history_challenges(db)
    
    def complete_challenge(self, id: int, db: Session):
        challenge = self.repo.get_challenge_by_id(id, db)
        if not challenge:
            raise HTTPException(status_code=404, detail="Challenge not found")

        challenge.status = "Completed"
        db.commit()
        db.refresh(challenge)

        return challenge
    
    def update_progress(self, db: Session, challenge_id: int, progress: int):
        return self.repo.update_progress(db, challenge_id, progress)