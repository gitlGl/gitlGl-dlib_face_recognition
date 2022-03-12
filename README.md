# gitlGl-dlib_face_recognition
# 基于dib图书馆人脸识别应用<br> 
1.人脸识别，活体识别（张嘴，眨眼 ）<br> 
2.人脸识别登录，注册。<br> 
3.批量用户导入数据库（将人脸向量特征转为二进制存入sqlite3，由于人脸向量特征是浮点数，转换成二进制会丢失精度），numpy==1.15.4，否则报错。<br> 
4.fps:5-10,cpu-i5-4210u,，gpu840m，编译测试过gpu加速，识别过程为少量计算，fps没有明显提高<br>
5.识别过程用了多进程并行，开始时识别速度慢（进程启动速度慢），考虑到登录速度问题人脸识别登录没有使用多进程，也没有加入活体识别,用qt重构多线程并行，效果估计很好<br>
6.ui框架为pyqt5<br>
7.内存占用500-600m，不懂怎么优化，不用多进程内存占用可以降到200-300m。<br>
8.人脸跟踪是耗时操作，去掉绘制框可提高fps。<br>
9.依赖<br>
dlib                    19.8.1<br>  
face-recognition        1.3.0<br>  
face-recognition-models 0.3.0 <br> 
imutils                 0.5.4 <br> 
numpy                   1.15.4 <br> 
opencv-python           4.5.5.62<br>  
psutil                  5.9.0 <br> 
PyQt5                   5.15.6<br>               
scipy                   1.5.4 <br> 
xlrd                    1.2.0 <br> 