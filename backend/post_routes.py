from fastapi import APIRouter, HTTPException
from post_models import PostCreate, Post
from database import posts_collection
from typing import List
from bson import ObjectId

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=Post)
async def create_post(post: PostCreate):
    try:
        post_dict = post.model_dump()
        result = await posts_collection.insert_one(post_dict)
        created_post = await posts_collection.find_one({"_id": result.inserted_id})
        if not created_post:
            raise HTTPException(status_code=404, detail="Created post not found")
        # Convert ObjectId to string in the response
        created_post["_id"] = str(created_post["_id"])
        return Post(**created_post)
    except Exception as e:
        print(f"Error creating post: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[Post])
async def get_posts():
    try:
        posts = await posts_collection.find().to_list(length=None)
        # Convert ObjectId to string in each post
        for post in posts:
            post["_id"] = str(post["_id"])
        return [Post(**post) for post in posts]
    except Exception as e:
        print(f"Error fetching posts: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
