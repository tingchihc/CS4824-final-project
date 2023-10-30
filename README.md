# Virginia Tech CS4824-final-project

[Report](https://github.com/ting-chih/CS4824-final-project/blob/main/final%20report.pdf)  
[Slides](https://github.com/ting-chih/CS4824-final-project/blob/main/final_presentation.pptx.pdf)

## G14 Members:  
Tingchih Chen, Huayu Liang, Zoe Zheng and Yilin Liu  

## Methods
We use Naive Bayes, Logistic Regression, SVM and NN to predict the news category.  

## Dataset
Our dataset is from MIcrosoft News Dataset (MIND) (https://msnews.github.io/).  
We extract the news title, abstract and category from MIND.  
Totally, we have 16 categories in our news dataset.  
We have 81,222 news in the training set(train.csv) and 20,305 news in the testing set(test.csv).  
 * For example:  
News(MLB's most problematic contracts: Miguel Cabrera's massive deal leads AL Central issues) => Category(sports)  

## 16 Categories  
autos, entertainment, finance, foodanddrink, health, kids, lifestyle, movies, music, news, northamerica, sports, travel, tv, video, weather.  


## Naive Bayes  
* Requirement: numpy, csv, pandas, math, sklearn, seaborn and product  
* Make sure your training set(train.csv) and testing set(test.csv) are in the correct root directory.  
* Then, you can run Naive Bayes.ipynb  
* Assessed the model’s performance using F1 score, accuracy, and confusion matrix, achieving a 63% accuracy.  

## Logistic Regression  
* Requirement: numpy, pandas, sklearn, matplotlib, seaborn
* Make sure the training set(train.csv) and testing set(test.csv) are in the correct root directory,  
* Then, you can run Logistic_Regression.ipynb  

## SVM
* Requirement: numpy, pandas, sklearn, matplotlib, seaborn
* Make sure the training set(train.csv) and testing set(test.csv) are in the correct root directory,  
* Then, you can run SVM.ipynb  

## Neural Network  
* Requirement: numpy, pandas, sklearn, matplotlib, seaborn, tensorflow, keras
* Make sure the training set(train.csv) and testing set(test.csv) are in the correct root directory,  
* Then, you can run Neural_Network.ipynb  
