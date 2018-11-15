# Adversarial Training
Initialization Technique for mapping Images with Text. Based on https://arxiv.org/pdf/1710.04087 's paper on cross-lingual word embeddings.

Below plot is generated for the setup of thetaD (Discriminator weights) trainable during mapping and considering mapping of questions to images, (to fool Discriminator) during mapping.

![alt_text](https://github.com/Murali81/Question-Relevance-in-Visual-QA/blob/master/Adversarial%20Training/Plots/epochs_35/plot_loss_trainD_always_true_textGen.PNG)

Generated for the setup of thetaD (Discriminator weights) NOT trainable during mapping and considering mapping of questions to images, (to fool Discriminator) during mapping.

![alt_text](https://github.com/Murali81/Question-Relevance-in-Visual-QA/blob/master/Adversarial%20Training/Plots/epochs_35/plot_loss_trainD_always_False_textGen.PNG)

Generated for the setup of thetaD (Discriminator weights) trainable during mapping and NOT considering mapping of questions to images, (to fool Discriminator) during mapping.

![alt_text](https://github.com/Murali81/Question-Relevance-in-Visual-QA/blob/master/Adversarial%20Training/Plots/epochs_35/plot_loss_trainD_True_NOtextGen.PNG)

Generated for the setup of thetaD (Discriminator weights) NOT trainable during mapping and NOT considering mapping of questions to images, (to fool Discriminator) during mapping.

![alt_text](https://github.com/Murali81/Question-Relevance-in-Visual-QA/blob/master/Adversarial%20Training/Plots/epochs_35/plot_loss_trainD_False_NOtextGen.PNG)


25 epochs Train-true always and No text.

![alt_text](https://github.com/Murali81/Question-Relevance-in-Visual-QA/blob/master/Adversarial%20Training/Plots/epochs_25/train_thetaD_NoTextGen.png)

#References

[1] Alexis Conneau, Guillaume Lample, Marc'Aurelio Ranzato, Ludovic Denoyer, Hervé Jégou, "Word Translation Without Parallel Data", Jan 2018, https://arxiv.org/pdf/1710.04087
