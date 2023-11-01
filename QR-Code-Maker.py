import qrcode

user_input = str(input("Enter Your Website including (https://): "))

if user_input.startswith("https://") or user_input.startswith("http://") and user_input.endswith(".net") or user_input.endswith(".com") or user_input.endswith(".info"):
    print("Website has been recognized")
  
else:
    print("Sorry use https or http with it")
img = qrcode.make(user_input)

type(img)
user_file_name = str(input("Enter The Name you want to save the file with extention also: "))

if user_file_name.endswith(".png") or user_file_name.endswith(".jpg"):
    print("the file has been saved")
    img.save(user_file_name)
  
else:
    print("Sorry you did not entered the extention")
