import os, sys
import ast
import google.protobuf as pf
import cv2
from PIL import Image as img
from PIL import ImageFont, ImageDraw, ImageEnhance
import cv2
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "api-key.json"
from retrieval import app
from google.cloud import vision
client = vision.ImageAnnotatorClient()


def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """


    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    objects = client.object_localization(
        image=image).localized_object_annotations
    im=img.open(path)
    w,h=im.size
    objs=[]
    classes=['Top','Jacket','Pants','Coat']
    for object_ in objects:
        print(object_)
        if object_.name in classes:
            a={}
            x=(object_.bounding_poly)
            x=str(x)
            print(x)
            x=x.split('\n')
            x1=x[1]
            y1=x[2]
            x2=x[9]
            y2=x[10]
            x1=x1.split(":")
            x1=x1[1]
            y1=y1.split(":")
            y1=y1[1]
            x2=x2.split(":")
            x2=x2[1]
            y2=y2.split(":")
            y2=y2[1]
            a['x1']=float(x1)*w
            a['x2']=float(x2)*w
            a['y1']=float(y1)*h
            a['y2']=float(y2)*h
            a['class']=object_.name
            a['confidence']=object_.score
            objs.append(a)

    return objs

def label_and_crop(path):
    obj=(localize_objects(path))
    print(obj)
    classes=['Top','Jacket','Pants','Coat']
    objs={}
    maxconf=0
    for i in obj:
        if i['class'] in classes and i['confidence']>maxconf:
            objs=i
            maxconf=i['confidence']
    a=[]
    print(objs['class'])
    a.append(objs)
    objs=a
    for i in objs:
        source_img = img.open(path).convert("RGB")
        draw = ImageDraw.Draw(source_img)
        draw.rectangle(((i['x1'],i['y1']), (i['x2'], i['y2'])), outline="black")
        draw.text((i['x1'],i['y1']-10),text=i['class'],fill="black")
        im=source_img.crop((i['x1'],i['y1'],i['x2'], i['y2']))
        source_img.save(path[0:len(path)-4]+"_boxed.jpg")
        im.save(path[0:len(path)-4]+"_cropped.jpg")
    return path[0:len(path)-4]+"_cropped.jpg"

if __name__ == "__main__":
	path=""
	while path!="exit":
		path=input("Enter image location: ")
		path="Category and Attribute Prediction Benchmark/"+path
		if path=="exit\n":
			break
		try:
			cropped_image=label_and_crop(path)
			cropped_image=cropped_image.split('/')
			cropped_image=cropped_image[1]
			app(cropped_image)
		except Exception as e:
			path=path.split('/')
			path=path[1]
			app(path)


