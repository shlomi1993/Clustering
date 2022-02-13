# Clustering

## Description
This repository documents my implementation in Python of K-Means clustering algorithm as part of Machine Learning course I took a Bar-Ilan University.

![image](https://user-images.githubusercontent.com/72878018/153747547-cc5110fa-5f90-4a6f-b448-7513c7371712.png)

_k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells. k-means clustering minimizes within-cluster variances (squared Euclidean distances), but not regular Euclidean distances, which would be the more difficult Weber problem: the mean optimizes squared errors, whereas only the geometric median minimizes Euclidean distances. For instance, better Euclidean solutions can be found using k-medians and k-medoids._

(source: https://en.wikipedia.org/wiki/K-means_clustering)



## Dataset

There are three main elements in the dataset of this RS:
1. Movies - the items to recommend.
2. Users - the entities that gets the recommendations.
3. Ratings - partial prior knowledge about users' prefrences.
Each user and each movie in the dataset is represented by a unique numeric identifier.

You can download the dataset from the directory "data" in this repo, and you are welcomed to change it as you wish.

Note: debugging and developping using the full dataset can take a lot of time, so you can use the smaller dataset in "data/debug".


## Requirements

To run the system, please make sure your machine can run Python 3.8 or above and the following packages are installed:
1. numpy
2. pandas
3. sklearn
4. matplotlib
To install the packages, use the command "pip3 install <package-name>" in the terminal/console.


## Program Parts
  
### Part 1 - Data
This part of the program prints essential information abour the dataset, and specifically about ratings.csv data file.
Data analysis based on ratings.csv:
1. Number of unique users: 21,244
2. Number of unique movies: 1,342
3. Number of ratings: 3,720,552
4. Minimal number of ratings given to a movie: 462
5. Maximal number of ratings given to a movie: 9,416
6. Minimal number of ratings a user gave: 46
7. Maximal number of ratings a user gave: 432
  
Ratings Distiburion:
  
![image](https://user-images.githubusercontent.com/72878018/153745187-d6a30455-c2cc-4396-838e-8b1e57b277ea.png)


### Part 2 - Collaborative Filtering
After the analysis in part 1, this part of the program is the implementation of the Collaborative-Filtering.
We will look at a user whose ID is 283225. We will extract the records that refer to him from the rating file, convert the movie IDs to titles and genres using the information from the movies_subset.csv, and we will get the following list:
 
![image](https://user-images.githubusercontent.com/72878018/153745720-bf2c26ac-12a0-4d25-a763-efaedf18301f.png)
  
It can be seen that the user gave a low rating to action movies, crime, mysteries, suspense, and gave a high rating to drama and romance movies. Therefore, we expect that the recommendation system will recommend drama and romance movies to the user more than other, and will avoid as much as possible recommendations on action movies, mystery crime and suspense.

We will run the recommendation system according to cf_user_based and with k = 5, and we will get the following results:
 
![image](https://user-images.githubusercontent.com/72878018/153745792-fe25d643-506a-4478-ab78-c67c2c7bc520.png)
  
Note: Match score is calculated by:
  
![image](https://user-images.githubusercontent.com/72878018/153745801-e72dfcd0-71cd-4854-baba-90b4c3ed02dd.png)
  
Where user_based_matrix is the (user-based) rating matrix, u is the user's index, and m is the movie's index. The division by 5 is meant to get the ratio versus the maximum rating, and the multiplication by 100 is meant to get a number in percent.
  
Now, we will use the information from the movies_subset.csv file to find the genres to which each of the five movies obtained from the recommendation system belongs and we will find that:
  
![image](https://user-images.githubusercontent.com/72878018/153745819-bbd0cc80-d2e6-4e95-b221-3baf0ecbbbe9.png)
 
The system did recommend drama and romance movies to the user. Please note that the user has also received recommendations for comedy movies, but these are also drama or romance movies, because the system must find the five movies that received the highest match score and return them. If there is no choice, it will not refrain from recommending a movie from a genre that the user did not like. Also, a movie may belong to both a genre that the user likes and a genre that it does not, so a movie match score may be high enough for the system to return the movie, even if the movie belongs to a genre that the user did not like.

  
### Part 3 - Evaluations
After analyzing the dataset and getting recommendations using the CF Recommender, we need to use some metrics to evaluate our system. 
In this part we will use 3 metrics for evaluations - P@k (with k=10), ARHR and RMSE.

![image](https://user-images.githubusercontent.com/72878018/153746164-4176c4dd-ec7d-43f7-918a-491aaa23d123.png)

  
The results are:  
![image](https://user-images.githubusercontent.com/72878018/153746012-1db88047-3d70-4148-8c3b-c0935562d060.png)
  
  
## Instructions

1. Make sure your system meet the requirements above.
2. Download the code and the dataset from this repo.
3. Open the terminal and run "python3 main.py"


## Screenshots

Program's output in a terminal:
  
![image](https://user-images.githubusercontent.com/72878018/153746867-5d2320da-2410-4b0e-9980-bbec76c66192.png)




In this repository I'll explain shortly about my centroids initialization process and then I'll present result graphs describing the average loss/cost value as a function of the iterations for K=2,4,8,16.
The Centroids Initialization Process:
I wrote a short program named "centroidsGenerator.py" that gets an integer number K as argument, generates K strings of 3 random floats between 0 to 1, and write them to an output file named "randomCents.txt".
Here is the code: 
 
To run ex1.py over every randomCents.txt file created (for K=2,4,8,16) I wrote the following script:
 
And then I launched the performance test using the command "./performanceTest.sh".

Results:
	Test number 1 - K=2:
 

	Test number 2 - K=4:
 

	Test number 3 - K=8:
 

	Test number 4 - K=16:
 


