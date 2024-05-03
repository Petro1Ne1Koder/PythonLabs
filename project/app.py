import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mtcnn import MTCNN

image = cv2.imread("test_image.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

detector = MTCNN()

faces = detector.detect_faces(image_rgb)

plt.figure(figsize=(10, 7))
plt.imshow(image_rgb)
ax = plt.gca()
for face in faces:
    x, y, w, h = face['box']
    rect = Rectangle((x, y), w, h, fill=False, color='red')
    ax.add_patch(rect)
plt.axis('off')
plt.show()


image = cv2.imread("test_image_2.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

detector = MTCNN()

faces = detector.detect_faces(image_rgb)

plt.figure(figsize=(10, 7))
plt.imshow(image_rgb)
ax = plt.gca()
for face in faces:
    x, y, w, h = face['box']
    rect = Rectangle((x, y), w, h, fill=False, color='red')
    ax.add_patch(rect)
plt.axis('off')
plt.show()


image = cv2.imread("test_image_3.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

detector = MTCNN()

faces = detector.detect_faces(image_rgb)

plt.figure(figsize=(10, 7))
plt.imshow(image_rgb)
ax = plt.gca()
for face in faces:
    x, y, w, h = face['box']
    rect = Rectangle((x, y), w, h, fill=False, color='red')
    ax.add_patch(rect)
plt.axis('off')
plt.show()
