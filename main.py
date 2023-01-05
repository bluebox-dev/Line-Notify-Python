from line_notify import LineNotify

ACCESS_TOKEN = "aLMbm7EhWNLiz4rY2ICUhkQskl5P1oY2lnkJIulV0kK"

notify = LineNotify(ACCESS_TOKEN)

notify.send("แจ้งเตือนภัย")

notify.send("คนร้าย", image_path='./1.png')


