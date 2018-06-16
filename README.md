# sw-kaggle

[![GitHub forks](https://img.shields.io/github/forks/yunshuipiao/sw-kaggle.svg)](https://github.com/yunshuipiao/sw-kaggle/blob/master/README.md)
[![GitHub forks](https://img.shields.io/github/stars/yunshuipiao/sw-kaggle.svg)](https://github.com/yunshuipiao/sw-kaggle/blob/master/README.md)
[![GitHub forks](https://img.shields.io/github/license/yunshuipiao/sw-kaggle.svg)](https://github.com/yunshuipiao/sw-kaggle/blob/master/README.md)

关于 kaggle 问题的解答与优化
* [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)
    * 主要工作：可视化分析不同特征与存活率的关系， 类别特征one-hot编码，数值特征分段处理，pipeline预处理数据, 使用LR， RF等进行投票分类，最终排名top10%  
              [[github]](https://github.com/yunshuipiao/sw-kaggle/blob/master/titanic/01.ipynb)
* [Digit Recognizer](https://www.kaggle.com/c/digit-recognizer)  
    * 主要工作：多分类问题，给定手写数字，进行0-9识别。分别使用numpy，tensorflow搭建ANN, CNN进行训练，识别率98%   
              [[github]](https://github.com/yunshuipiao/sw-kaggle/blob/master/digit_recognizer/07-ann-cnn-rnn.ipynb)
* [Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs)
    * 主要工作：使用nltk， sklearn，构建关于问题特征的向量进行相似性判断,采用lightgbm进行训练，完成相似问题判断。   
              [[github]](https://github.com/yunshuipiao/sw-kaggle/blob/master/quora-question-pairs/01.ipynb)
* [机器学习之红楼梦作者判断](https://github.com/yunshuipiao/SWBlog/blob/master/maching_learning/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%B9%8B%E7%BA%A2%E6%A5%BC%E6%A2%A6%E4%BD%9C%E8%80%85%E5%88%A4%E6%96%AD(%E4%B8%80%EF%BC%9AKMeans).md)  
    * 主要工作：针对全书每一章节进行分词，tf-idf文档向量化，分别使用监督和无监督进行训练预测， 并与其它名著对比结果。  
              [[github]](https://github.com/yunshuipiao/sw-kaggle/blob/master/experimental/sidamingzhu/01.ipynb)

