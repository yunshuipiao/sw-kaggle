## 1：
采用RNN神经网路训练实现。  
代码和训练过程见github链接：https://github.com/yunshuipiao/sw-kaggle/blob/master/digit_recognizer/05.ipynb

其最后一次输出为训练后的预测输出：

![](https://user-gold-cdn.xitu.io/2018/5/20/1637c80baacd44d8?w=769&h=266&f=png&s=34335)   
最后结果： 144+177=321.

----

## 2.
在最近训练DL(比如手写数字识别和如上的RNN实现加法器)的过程中：
* 手写数字识别：
参数难以调试，训练速度慢。因此在调节参数方面花了时间。另外减少了隐藏层及其神经元的个数，加快训练。
* 加法器：
相比而言，训练速度很快。困难主要在参数难以调节上。比如隐藏层设置不同的神经元， 不同的学习速率对结果的影响。都是采用RandomizedSearchCV的思路解决的：首先对需要调节的参数给定大概的范围，逐渐逼近最优解。

## 3.
目前由于DL不像传统的machine learning algorithm一样，有很完善的理论支撑。另外一个是不知道众多隐藏中包含了什么信息， 为什么结果会有效，因此从使用上来说，对使用者的数学性要求不高，也可以进行调参。
对于我而言，目前了解最基本的传统机器学习方法，正在深入了解其背后的数学原理及推导。而对神经网络的可解释性也保持足够大的好奇心，以便更了解，更快的用好神经网络。

## 附加题：
由于之前写过kaggle相关的入门题目，因此直接使用了提供的数据训练集。  
其中90%用于训练， 10%用于测试。其神经网络结构见最后图片。  
部分训练结果如下：  
在kaggle提交了几次结果，score分别为和87%和94%。后面分数提高的原因在于对特征进行MinMaxScaler。  
代码见github链接:https://github.com/yunshuipiao/sw-kaggle/blob/master/digit_recognizer/03.ipynb  

部分训练结果如下：
![](https://user-gold-cdn.xitu.io/2018/5/20/1637cb4b3e5b0fbb?w=560&h=196&f=png&s=51498)

神经网络结构：
![](https://user-gold-cdn.xitu.io/2018/5/20/1637cb75ccbb8580?w=1440&h=1080&f=jpeg&s=185461)

参考资料：  
[Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/index.html)  
  [Anyone Can Learn To Code an LSTM-RNN in](http://iamtrask.github.io/2015/11/15/anyone-can-code-lstm/)
