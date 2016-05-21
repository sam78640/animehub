import os
for i in range(1,153):
    try:
        if i > 9 and i < 100:
            number = "0"+str(i)
            os.system("ffmpeg -i "+number+".mp4 -r 20 "+number+".avi -y")
            os.remove(number+".mp4") 
        if i > 99:
            number = str(i)
            os.system("ffmpeg -i "+number+".mp4 -r 20 "+number+".avi -y")
            os.remove(number+".mp4")
        if i <= 9:
            number = "00"+str(i)
            os.system("ffmpeg -i "+number+".mp4 -r 20 "+number+".avi -y")
            os.remove(number+".mp4")
    except:
        print ("error while conversion ask sameer")
