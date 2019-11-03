import matplotlib.pyplot as plt

x_3 = [837.7344970703125, 835.8549194335938, 837.2323608398438]
y_3 = [1313.5133056640625, 1311.461181640625, 1309.1494140625]
x_4 = [802.1984252929688, 802.7943115234375, 803.0742797851562]
y_4 = [1322.4844970703125, 1327.3150634765625, 1324.919677734375]
x_5 = [781.8235473632812, 779.491943359375, 779.7608032226562]
y_5 = [1366.61181640625, 1365.9052734375, 1361.903076171875]
x_6 = [765.63720703125, 763.0408325195312, 754.2750244140625]
y_6 = [1409.5079345703125, 1409.2236328125, 1414.6978759765625]

x_5 = [233.0236053466797,
    233.6308135986328,
    233.6023406982422,
    233.99703979492188,
    234.74021911621094]
y_5 = [1272.958740234375,
    1273.3983154296875,
    1271.096435546875,
    1268.8427734375,
    1266.672607421875]
x_0 = [252.43814086914062,
    252.47767639160156,
    252.32786560058594,
    252.66844177246094,
    251.3201904296875]
y_0 = [1293.75,
    1295.953125,
    1296.8243408203125,
    1300.2333984375,
    1296.66259765625]

#plt.scatter(y=[1200-item for item in x_3], x=y_3, label="Cell_ID #3")
#plt.scatter(y=[1200-item for item in x_4], x=y_4, label="Cell_ID #4")
plt.scatter(y=[1200-item for item in x_5], x=y_5, label="Cell_ID #85")
plt.scatter(y=[1200-item for item in x_0], x=y_0, label="Cell_ID #90")
#plt.ylim(0, 1200)
#plt.xlim(0, 1600)
plt.legend()
plt.show()
plt.close()
