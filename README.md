### **Introduction**
* The model is trained on the eminst dataset consisting of capital letters and numbers.
* The model is able to correctly predict images with dimensions (28 x 28 x 1).
* Prediction accuracy is about 92%

### **Web UI**
![Web UI](https://github.com/ntnhan-ds/digits_letters_recognition/blob/main/ui_image.png)

### **Limited**
* Because the model is only trained in the eminst dataset. Therefore, the data is not enough to be able to identify all other characters on the outside.
* Image processing may cause the image to not retain all details such as: size, number of channels,... . This reduces performance.

### **Development**
* Increase the amount of data and the data needs to be more diverse so the model can accurately recognize more characters.
* Upgrade the system to recognize capcha.