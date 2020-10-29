# Labwork 3

## Binarization

**1.Arbitrary threshold**

Looking at the images, we can pick 100 for the threshold value for the *forme1* image and 120 for the *house* image. When we apply image thresholding, we get theses result:

![](./LabWork_3/Result/forme1_bin.png =200x200)
![](./LabWork_3/Result/house8_bin.png =200x200)

The result for these 2 pictures are pretty good just by guessing a arbitrary value. Still this method is very uneffective, the first picture contains some aritifact and the object isn't very clean. When we continue to apply this technique for the *femme* picture, it isn't easy to guess the threshold value like the others two. Here is the result when the threshold value is 125:

![](./LabWork_3/Result/femme_bin.png =200x200)

The woman's face has lost many detail, especially her hair is completely unrecognizeable. So we can see this technique is very inaccurated. When we try to it use with images that have subject and background color value closed together, the result are very imprecise.

**2.Threshold with the histogram**

![alt](./LabWork_3/Result/forme1_hist.png =400x)
![](./LabWork_3/Result/house8_hist.png =400x)

When we plot the histogram of the first 2 images, the histograms show in all 2 pictures very distince peaks. Now is much more easy to choose the optimal threshold.
For the *forme1* image, the value is 127 and for the *house* image, we could choose the value 110.

![](./LabWork_3/Result/forme1_binwithhist.png =200x200)
![](./LabWork_3/Result/house8_binwithhist.png =200x200)

The result this time is better than the previous one, the objects in both images are complete and distinc from the background. And here is the histogram for the *femme* image:

![](./LabWork_3/Result/femme_hist.png =400x)

This time, the histogram show the pixels intensity focus mainly at the middle of the graph (100-127), it's not easy to find an optimal threshold value in this situation. 

Let apply this technique to the *forme3* picture, from the histogram below, we could choose the value 130 for threshold.

![](./LabWork_3/Result/forme3_hist.png =400x)

Result:

![](./LabWork_3/Result/forme3_binwithhist.png =200x200)

The T-shape object is still being blend with the dark side background. This is because, the lighting on the T-Shape object is not uniform, thus resulted in half side of the object still blend in with the darker corner. Base on this property, we can conclude that binarization with histogram work best only on picture in which the object has very obvious distinctive color that seperate it from the background and share the same amount of light across all the picture.

**3.Thresholding by the Otsu method**

Add the extra flag `cv.THRESH_OTSU` to the thresholding function to make it determinates the threshold value automatically:

![](./LabWork_3/Result/forme1_bin_otsu.png =200x200)
![](./LabWork_3/Result/forme3_bin_otsu.png =200x200)

The threshold values determinated by the algorithm for the 2 pictures, respectively are 120 and 140, which is not too different compare to our previous values.

## Application exercises

**1. Text extraction**
It can be see clearly, the text are black and their surrounding is much brighter, we can apply binarization with the thresholding function, using otsu method or histogram to determinate it threshold value. For this picture, the threshold value is about 170

![](./LabWork_3/Result/cadastre1_bin.png =400x400)
**2. Extraction of objects**



