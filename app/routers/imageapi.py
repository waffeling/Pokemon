from fastapi import FastAPI, Response, status, Request
from minio import Minio
from fastapi import APIRouter

router = APIRouter()

#opening client to access server
client = Minio("minio:9000",
access_key="adminuser",
secret_key="pass123456",
secure=False
)


@router.get("/img/{image_id}")
def image_return(image_id):

    bucket_name = "card-images"

    found = client.bucket_exists(bucket_name)
    if not found:
        print("Created bucket", bucket_name)
        return "Bucket doesn't exist"

    try:
        response = client.get_object("card-images", image_id)
        
    except Exception as e:
        return str(e)

    finally:
        image = response.data
        
        response.close()
        response.release_conn()
    
    return Response(content=image, media_type="image/jpeg")

    