# Line-Notify-Python

<img align="center" alt="GIF" src="https://github.com/bluebox-dev/Line-Notify-Python/blob/main/logo.png" height="320" />


## Reference in Doc
* **Source of this Workshop description:**
[Doc]()

## How to use this Workshop
```
## install python package.
pip install line_notify

## run program after edit token ago.
python main.py
```

### Configuration Code
> Assuming the following **Edit Config** as token in main.conf :
```
from line_notify import LineNotify

ACCESS_TOKEN = "-> Token Line <-"

notify = LineNotify(ACCESS_TOKEN)
```

> Send message to Line 
```
## message only
notify.send("แจ้งเตือนภัย")

## message + image 
notify.send("คนร้าย", image_path='./1.png')
```