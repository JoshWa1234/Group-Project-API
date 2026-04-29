from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from schema.challenge_schema import ChallengeCreateRequest, ChallengeResponse, ChallengeProgressUpdateRequest
from services.challenge_service import ChallengeService


router = APIRouter(prefix="/challenges", tags=["challenges"])
service = ChallengeService()


@router.post("/", response_model=ChallengeResponse)
def create_challenge(
    challenge: ChallengeCreateRequest,
    db: Session = Depends(get_db)
):
    return service.create_challenge(db, challenge)


@router.get("/", response_model=List[ChallengeResponse])
def get_all_challenges(db: Session = Depends(get_db)):
    return service.get_all_challenges(db)


@router.get("/in-progress", response_model=List[ChallengeResponse])
def get_in_progress_challenges(db: Session = Depends(get_db)):
    return service.get_in_progress_challenges(db)

@router.put("/{challenge_id}/retire", response_model=ChallengeResponse)
def retire_challenge(
    challenge_id: int,
    db: Session = Depends(get_db)
):
    challenge = service.retire_challenge(db, challenge_id)

    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")

    return challenge

@router.get("/history", response_model=list[ChallengeResponse])
def get_history_challenges(db: Session = Depends(get_db)):
    return service.get_history_challenges(db)

@router.put("/{id}/complete", response_model=ChallengeResponse)
def complete_challenge(id: int, db: Session = Depends(get_db)):
    return service.complete_challenge(id, db)

@router.put("/{challenge_id}/progress", response_model=ChallengeResponse)
def update_challenge_progress(
    challenge_id: int,
    progress_update: ChallengeProgressUpdateRequest,
    db: Session = Depends(get_db)
):
    challenge = service.update_progress(
        db,
        challenge_id,
        progress_update.progress
    )

    if not challenge:
        raise HTTPException(status_code=404, detail="Challenge not found")

    return challenge