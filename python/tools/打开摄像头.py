import cv2


class Catch(object):

    def __init__(self, device_id=0):

        self.device_id = device_id
        self.capture = cv2.VideoCapture(self.device_id)  # 打开摄像头

    def read(self):

        __, frame = self.capture.read()
        __ = self.capture.set(3, 320)  # 设置宽
        __ = self.capture.set(4, 240)   # 设置高

        colour = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # cv2.COLOR_RGBA2RGB
        return colour

    def handle(self, colour):
        colour = cv2.findContours(colour)
        hull = cv2.convexHull(colour, returnPoints=False)
        return cv2.convexityDefects(colour, hull)


if __name__ == '__main__':

    C = Catch()
    while True:
        X = C.read()
        print(X)
        # print(type(C.handle(X)))
        cv2.imshow('frame', X)
        if cv2.waitKey(1) == ord('q'):  # 设置按Q退出
            break


# # 打开摄像头并灰度化显示
# import cv2
#
# capture = cv2.VideoCapture(0)
#
# while True:
#     # 获取一帧
#     ret, frame = capture.read()
#     print(ret)
#     # 将这帧转换为灰度图
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     print(gray)
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) == ord('q'):
#         break

