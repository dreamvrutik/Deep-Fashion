# Deep Fashion
 Deep Fashion app created using PYTHON

 This app is created for cloth suggestion. The app takes input from the user which is the path to image on your local machine , then it passes the image through Object Detection Model which detects the clothes present in the image and crops the image to fashion apparel with highest confidence.

 This cropped image is then passed to other model which takes the cropped image as an input and finds similar matching images in the database.

 The image is matched with other images on the basis of following three things :
    1. Color
    2. Shape
    3. Pattern

  Then the top 5 images matching the input image apparel are shown along with the cropped apparel image.

  Following are the examples tested with our model :

  Input 1:
    ![Image of Input1](Img1.jpg?raw=true "Input 1")
    ![Image of Input1 Boxed](Img1_boxed.jpg?raw=true "Input 1 Boxed")
    ![Image of Input1 Cropped](Img1_cropped.jpg?raw=true "Input 1 Croppped")
    ![Image of Input1 Result](Img1Result.png?raw=true "Input 1 Result")


  Input 2:
    ![Image of Input2](Img2.jpg?raw=true "Input 2")
    ![Image of Input2 Boxed](Img2_boxed.jpg?raw=true "Input 2 Boxed")
    ![Image of Input2 Cropped](Img2_cropped.jpg?raw=true "Input 2 Croppped")
    ![Image of Input2 Result](Img2Result.png?raw=true "Input 2 Result")
