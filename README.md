# rpibeadsort
try simplest setup for beadsorting. the prototype is build out of carcdboard one raspberry pi with a camera and four servos.
there are following modules now: 
one servo free rotating for queueing the beads into a straw. 
one servo for blocking the queue infront of the window 
one servo blocking the bead from leaving the window and releasing it into the selector straw and 
one servo to select a bucket. 


# dependancies
installed 
```
pip3 install opencv-contrib-python && pip3 install scikit-image && pip3 install pillow && pip3 install imutils 
ln -sf /usr/bin/python3.5 /usr/bin/python
apt-get install -y libhdf5-serial-dev
apt-get install -y libopenblas-dev libatlas-base-dev liblapack-dev gfortran
apt-get install -y build-essential cmake unzip pkg-config gcc-6 g++-6 
apt-get install -y libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
apt-get install -y libjpeg-dev libpng-dev libtiff-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev
sudo apt-get -y install libgtk2.0-dev libtbb-dev qt4-default
pip3 install matplotlib && pip3 install progressbar2 && pip3 install beautifulsoup4 && pip3 install pandas
```


