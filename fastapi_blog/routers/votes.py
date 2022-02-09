from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import schemas, database, models, oauth2

'''
sqlalchemy
func -> count ,같은 함수 위해
label -> as  , 컬럼 이름 변경
'''

router = APIRouter(
    prefix="/votes",
    tags=["votes"]
)


@router.post('/', status_code= status.HTTP_201_CREATED)
def create_vote(req : schemas.Votes , db : Session = Depends(database.get_db) , 
current_user : int = Depends(oauth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == req.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
        ,detail= f"Post with id : {req.post_id} does not exsist")
    vote_query =db.query(models.Votes).filter(
        models.Votes.post_id == req.post_id , models.Votes.user_id == current_user.id
    )
    found_vote = vote_query.first()
    if req.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                detail=f"user {current_user.id} has alredy voted on post {req.post_id}")
        new_votes = models.Votes(post_id = req.post_id , user_id = current_user.id)
        db.add(new_votes)
        db.commit()
        return {"message"  :  "successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        vote_query.delete(synchronize_session= False)
        '''
        synchronize_session = evaluate
        → 파이썬에 생성된 쿼리를 곧바로 평가해서 세션으로부터 제거되어야 할 객체를 결정. 기본값이고 효율적이지만 견고하지 않고, 복잡한 쿼리는 evaluate 될 수 없다.
        synchronize_session = fetch
        → 삭제되기 전에 select 쿼리를 수행하고 해당 결과를 사용해서 어떤 객체들이 세션에서 삭제되어야할지 결정. 덜 효율적이지만 유효한 쿼리를 다룰 수 있다.

        synchronize_session = False
        → 세션 갱신을 시도하지 않기 떄문에 매우 효율적이다. 그러나 삭제한 후에 세션을 사용하려고 하면 부정확한 결과를 얻을 수 있다.
        '''

        db.commit()
        return {"message" : "successfully deleted vote"}