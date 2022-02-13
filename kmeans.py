# Shlomi Ben-Shushan

import matplotlib.pyplot as plt
import numpy as np
import sys

EPOCHS = 20

# Read image and reshape it to a matrix of pixels.
pixels = plt.imread(sys.argv[1]).astype(float) / 255.
pixels = pixels.reshape(-1, 3)
total = float(len(pixels))

# Initialize centroids.
centroids = np.loadtxt(sys.argv[2])
k = len(centroids)

# Create output log file.
log_file_name = sys.argv[3]
open(log_file_name, "w").close()
log = open(log_file_name, "a")

previous_centroids = None
iterations = 0
losses = []

# K-Means algorithm:
for iter in range(EPOCHS):
    if np.array_equal(centroids, previous_centroids):
        break
    iterations += 1
    previous_centroids = centroids.round(4)
    mapper = {}
    loss = 0;
    for pixel in pixels:
        distances = []
        for centroid in centroids:
            distance = pow(np.linalg.norm(centroid - pixel), 2) # According to ||xi-zj||^2_2.
            distances.append(distance)
        min_distance = min(distances)
        i = distances.index(min_distance)
        if i in mapper:
            mapper[i].append(pixel)
        else:
            mapper[i] = [pixel]
        loss += min_distance;
    for key in mapper.keys():
        centroids[key] = np.average(mapper[key], axis=0);
    losses.append(loss / total)
    centroids = centroids.round(4)
    log.write(f"[iter {iter}]:{','.join([str(i) for i in centroids])}" + "\n")

log.close()

# Use matplotlib.pyplot library to create a graph and display it.
plt.plot(range(iterations), losses)
plt.title("The average/total loss with K = " + str(k))
plt.xlabel("iteration")
plt.ylabel("avg/total loss")
plt.show()