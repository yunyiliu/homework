import numpy as np
import pandas as pd
%matplotlib inline
from matplotlib import pyplot as plt
import cv2
import os
# INPUT PATHS:
BASE = '../input/att-database-of-faces/'
img = cv2.imread(BASE + 's1/1.pgm', 0) # '0' for reading grayscale images

IMG_SHAPE = img.shape

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('A random grumpy person')
plt.show()
filepaths = [1,1] # Contains the absolute paths of all the image files
for s_i in os.listdir(BASE): # The folders containing the files are labelled as s1, s2, etc
    if s_i != 'README': # There is also a README file present in the data, this must be ignored
        for filename in os.listdir(BASE + s_i):
            filepaths.append(BASE + s_i + '/' + filename)

df = pd.DataFrame({'filepaths':filepaths})
display(df)
image_count = len(filepaths)
print(image_count)

image_count = len(filepaths)
print(image_count)

i = 0


train_data = []
test_date = []
for item in df:
	if(i % 3 == 0 && i < image_count) {
		train_data[i] = item
	} else {
		test_data[i] = item
	}
	i = i + 1

convolutional_model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

convolutional_model.fit(
  train_data,
  validation_data=val_ds,
  epochs=15
)

loss, acc = convolutional_model.evaluate(test_data)
print("test accuracy:", acc)
