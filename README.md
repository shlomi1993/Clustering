# Clustering

## Description
This repository documents my implementation in Python of K-Means clustering algorithm for Image Compression task as part of Machine Learning course I took a Bar-Ilan University.

<p align="center"><img src=https://user-images.githubusercontent.com/72878018/153747547-cc5110fa-5f90-4a6f-b448-7513c7371712.png width=700></p>

_k-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. This results in a partitioning of the data space into Voronoi cells. k-means clustering minimizes within-cluster variances (squared Euclidean distances), but not regular Euclidean distances, which would be the more difficult Weber problem: the mean optimizes squared errors, whereas only the geometric median minimizes Euclidean distances. For instance, better Euclidean solutions can be found using k-medians and k-medoids._

(source: https://en.wikipedia.org/wiki/K-means_clustering)


## Dataset

The input is an image of a dog, so we can say that the dataset is an array of pixels.

<p align="center"><img src=https://user-images.githubusercontent.com/72878018/153747717-a34c3045-72c7-4687-a1fe-516c5f828874.png width=700></p>


## Requirements

To run the system, please make sure your machine can run **Python 3.8** or above and the following packages are installed:
1. numpy
2. matplotlib
To install the packages, use the command "pip3 install <package-name>" in the terminal/console.


## Program Report

I'll explain shortly about the centroids initialization process and then I'll present result graphs describing the average loss/cost value as a function of the iterations for K=2,4,8,16.

#### The Centroids Initialization Process:
By using the short program "centroidsGenerator.py" (in this repo) that gets an integer number K as an argument, we can generate K strings of 3 random floats between 0 to 1, and write them to an output file named "randomCents.txt".
 
#### Results:


![image](https://user-images.githubusercontent.com/72878018/153748228-f30e51da-8e40-419c-84e6-8c54f58c0be9.png)


## Instructions

To run the program:
1. Make sure your system meets the requirements above.
2. Download the code and the dataset from this repo.
3. Open the terminal and run "python3 kmeans.py dog.jpeg randomCents.txt out.txt"

You can use different centroids initialization files or output log files.


## Screenshots

Program's output log file content after running the algorithm with 2 centroids:
	
![image](https://user-images.githubusercontent.com/72878018/153748171-f7901890-632e-46c8-86e1-49cdbfd0c98c.png)
	
We can see that the algorithm converged after 9 epochs.
