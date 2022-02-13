# Clustering

## Description
This repository documents my implementation in Python of K-Means clustering algorithm for Image Compression task as part of Machine Learning course I took a Bar-Ilan University.

![image](https://user-images.githubusercontent.com/72878018/153747547-cc5110fa-5f90-4a6f-b448-7513c7371712.png)

_k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells. k-means clustering minimizes within-cluster variances (squared Euclidean distances), but not regular Euclidean distances, which would be the more difficult Weber problem: the mean optimizes squared errors, whereas only the geometric median minimizes Euclidean distances. For instance, better Euclidean solutions can be found using k-medians and k-medoids._

(source: https://en.wikipedia.org/wiki/K-means_clustering)


## Dataset

The input is an image of a dog, so we can say that the dataset is an array of pixels.

![image](https://user-images.githubusercontent.com/72878018/153747717-a34c3045-72c7-4687-a1fe-516c5f828874.png)


## Requirements

To run the system, please make sure your machine can run **Python 3.8** or above and the following packages are installed:
1. numpy
2. matplotlib
To install the packages, use the command "pip3 install <package-name>" in the terminal/console.


## Program Report

I'll explain shortly about centroids initialization process and then I'll present result graphs describing the average loss/cost value as a function of the iterations for K=2,4,8,16.

#### The Centroids Initialization Process:
By using the short program "centroidsGenerator.py" (in this repo) that gets an integer number K as argument, we can generate K strings of 3 random floats between 0 to 1, and write them to an output file named "randomCents.txt".
 
#### Results:
	
Test number 1 - K=2:
	
![image](https://user-images.githubusercontent.com/72878018/153748080-74915e12-b20e-4a52-8223-795f5921164d.png)

	
Test number 2 - K=4:
	
![image](https://user-images.githubusercontent.com/72878018/153748083-e979f866-00ab-4118-835c-b8b482437f4b.png)


Test number 3 - K=8:
	
![image](https://user-images.githubusercontent.com/72878018/153748089-c9ea78df-a60f-4666-aa01-0532a98e0835.png)

	
Test number 4 - K=16:
	
![image](https://user-images.githubusercontent.com/72878018/153748091-139d9102-15f8-4c2a-9114-98d1c4590bfe.png)


## Instructions

1. Make sure your system meet the requirements above.
2. Download the code and the dataset from this repo.
3. Open the terminal and run "python3 kmeans.py dog.jpeg randomCents.txt out.txt"

You can use different centroids initialization file or output log file.


## Screenshots

Program's output in a terminal:
![image](https://user-images.githubusercontent.com/72878018/153748171-f7901890-632e-46c8-86e1-49cdbfd0c98c.png)
