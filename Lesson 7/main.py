import os
import cv2
from PIL import Image

os.chdir("C:\Users\Harshit\Downloads\Anay\JetLearn\OpenCV\Lesson 7\images")
path = "C:\Users\Harshit\Downloads\Anay\JetLearn\OpenCV\Lesson 7\images"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir(path))

for file in os.listdir("."):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print(mean_width)
print(mean_height)

for file in os.listdir('.'):

    if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):

        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)

        imgResized = img.resize(mean_width, mean_height), Image.PIL.Image.LANCZOS
        imgResized.save(file, "JPEG", quality = 95)
        print(img.filename.split("\\")[-1], " is resized")


def videogenerator():
    video_name = "MyFirstVideo.avi"

    os.chdir("C:\Users\Harshit\Downloads\Anay\JetLearn\OpenCV\Lesson 7\images")

    images = []

    for file in os.listdir("."):
        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
            images.append(file)
    
    print(images)

    frame = cv2.imread(os.path.join(".", images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(".", image)))
    
    cv2.destroyAllWindows()
    video.release()

videogenerator()
