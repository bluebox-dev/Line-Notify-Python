from line_notify import LineNotify

ACCESS_TOKEN = "aLMbm7EhWNLiz4rY2ICUhkQskl5P1oY2lnkJIulV0kK"

notify = LineNotify(ACCESS_TOKEN)

notify.send("แจ้งเตือนภัย")

notify.send("คนร้าย", image_path='./1.png')


## Function
def SendTxt(str):
    notify.send(str)
    
## Function
def SendImage(txt, path):
    notify.send(txt, image_path=path)

## Add to yolov5
# if int(cls)== 67:
#    ln.SendTxt(int(cls))
#    cv2.imwrite("img.jpg", imc)
#    ln.SendImage(str(cls), "img.jpg")
