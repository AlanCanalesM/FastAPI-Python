from ..database import User
from ..database import Movie
from ..database import userReviews
from ..schemas import ReviewRequestModel
from ..schemas import ReviewResponseModel
from fastapi import HTTPException
from ..schemas import ReviewUpdateModel
from fastapi import APIRouter
from typing import List

router = APIRouter(prefix='/api/v1/reviews')


@router.post('', response_model=ReviewResponseModel)
async def create_review(review: ReviewRequestModel):

    if User.select().where(User.id == review.user_id).first() is None:
        raise HTTPException(404, 'User not found')

    if Movie.select().where(Movie.id == review.movie_id).first() is None:
        raise HTTPException(404, 'Movie not found')

    user_review = userReviews.create(
        user_id=review.user_id,
        movie_id=review.movie_id,
        review=review.review,
        score=review.score
    )

    return user_review


@router.get('', response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1, lim: int = 10):

    reviews = userReviews.select().paginate(page, lim)  # Select * From userReviews;

    return [user_review for user_review in reviews]


@router.get('/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):

    user_review = userReviews.select().where(userReviews.id == review_id).first()

    if user_review is None:

        raise HTTPException(404, 'Review not found')

    return user_review


@router.put('/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id: int, new_review: ReviewUpdateModel):

    user_review = userReviews.select().where(userReviews.id == review_id).first()

    if user_review is None:

        raise HTTPException(404, 'Review not found')

    user_review.review = new_review.review
    user_review.score = new_review.score

    user_review.save()

    return user_review


@router.delete('/{review_id}', response_model=ReviewResponseModel)
async def delete_review(review_id: int):
    
    user_review = userReviews.select().where(userReviews.id == review_id).first()

    if user_review is None:

        raise HTTPException(404, 'Review not found')

    user_review.delete_instance()

    return user_review