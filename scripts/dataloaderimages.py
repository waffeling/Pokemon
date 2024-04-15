from minio import Minio
import os

image_dir = "C:\\Users\\cock\\Desktop\\Pokemon Card Images\\Paldean_Fates"

def get_pokemon_list(file_path:str):
    files = os.listdir(file_path)
    jpg_list = []
    for i in files:
        period = i.find('.')
        if i[period+1::] == 'jpeg':
            jpg_list.append(i)
   
    return jpg_list


#get pokemon image filenames
image_list = get_pokemon_list(image_dir)

#opening client to access server
client = Minio("localhost:9000",
access_key="adminuser",
secret_key="pass123456",
secure=False
)

# The destination bucket and filename on the MinIO server
bucket_name = "card-images"


found = client.bucket_exists(bucket_name)
if not found:
    client.make_bucket(bucket_name)
    print("Created bucket", bucket_name)
else:
    print("Bucket", bucket_name, "already exists")

print(image_list)
#Create a loop to update all the files in image_dir
for i in range(len(image_list)):

    destination_file = image_list[i]
    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, image_dir+"\\"+image_list[i],
    )
    print(
        image_dir+"\\"+image_list[i], "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )