**VQG Image Captioning InceptionV3.ipynb**
Jupyter notebook file has everything coded in it, which I hope makes it easy to understand the code. VQG - Visual Question Generation Dataset is used to generate natural questions.

Run the **prepare_dataset.ipynb** file to create train,test,val splits and dataset format. I made my dataset similar to Flickr8k dataset format.

I am using Beam search with **k=3, 5, 7** and an Argmax search for predicting the captions of the images.

Model is trained till a loss value of **3.0077** had been achieved, which gives considerably good results. You can check out some examples below. The rest of the examples are in the jupyter notebook. You can run the Jupyter Notebook and try out your own examples. 
*unique.p* is a pickle file which contains all the unique words in the vocabulary. 

# Dependencies

* Keras 2.0.8
* Tensorflow 1.7.0
* tqdm
* numpy
* pandas
* matplotlib
* pickle
* PIL
* glob

# References

[1] M. Hodosh, P. Young and J. Hockenmaier (2013) "Framing Image Description as a Ranking Task: Data, Models and Evaluation Metrics", Journal of Artificial Intelligence Research, Volume 47, pages 853-899 <a href="http://www.jair.org/papers/paper3994.html">http://www.jair.org/papers/paper3994.html</a> 

[2] Oriol Vinyals, Alexander Toshev, Samy Bengio, Dumitru Erhan <a href="https://arxiv.org/abs/1411.4555">Show and Tell: A Neural Image Caption Generator</a>

[3] CS231n Winter 2016 Lesson 10 Recurrent Neural Networks, Image Captioning and LSTM <a href="https://youtu.be/cO0a0QYmFm8?t=32m25s">https://youtu.be/cO0a0QYmFm8?t=32m25s</a> 


