def echo(in_string):
    print(in_string)


//While 반복문
switch = True
while (switch):
    in_text = input("메아리 내용 : ")
    if (in_text == "끝"):
        switch = False
    else:
        echo(in_text)
print("end")
