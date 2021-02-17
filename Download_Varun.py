## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import time # to sleep the thread
import os

for x in range(138, 150):
    time.sleep(65.0)
    # Set up the image URL and filename
    image_url = "https://dcc.ussgroup.co.uk/images/dutmc_35.jpg"
    filename = image_url.split("/")[-1]
    filename = filename.split(".")[0]+"_{}.jpg".format(x)

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)
    path = os.path.join("C:/Users/varun/Python/ACSEF_2021/Images/{}".format(filename))

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.

        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(path,'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')