from gpiozero import Button
take_pic_btn = Button(14)
take_pic_btn.when_pressed = take_picture
def take_picture():
    print("Take a picture")
