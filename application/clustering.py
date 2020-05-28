"""	
Created on Tue Feb 11 22:45:21 2020	
@author: Mahedi MAHALAL	
inspired from https://github.com/mahesh147/KMeans-Clustering	
"""	
# K-Means Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

#Importing the mall dataset with pandas.

class Clustering():

    ####################### class to print clustering ##########################

    def __init__(self, filename, start_column, end_column):
        self.n = start_column
        self.m = end_column
        self.filename = filename
        self.dataset = pd.read_csv(self.filename)
        self.X = self.dataset.iloc[:,[self.n,self.m]].values

    #def  return_x(self):
        ######## return concerned columns of the dataset ########
       #return self.X


    def print_elbow(self, number_of_k):
        # Plot the graph to visualize the Elbow Method to find the optimal number of cluster
        self.k = number_of_k
        wcss=[]
        silhouette_values = {}
        for i in range (2,self.k):
            self.kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter=300, n_init = 10, random_state =None)
            self.kmeans.fit(self.X)
            wcss.append(self.kmeans.inertia_) # Sum of squared distances of samples to their closest cluster center.
            # Compute the silhouette scores for each sample
            cluster_labels = self.kmeans.fit_predict(self.X)
            silhouette_avg = silhouette_score(self.X, cluster_labels)
            silhouette_values[i] = silhouette_avg
            print("For n_clusters =", i,"The average silhouette_score is :", silhouette_avg)

        print("Best silhouette score:", max(silhouette_values, key=silhouette_values.get))

        plt.plot(range(2,self.k),wcss)
        plt.title('The Elbow Method')
        plt.xlabel('Number of clusters')
        plt.ylabel('WCSS')
        plt.show()
        return

    def print_kmeans(self, Optimal_k):
        plt.style.use('seaborn-deep')
        # Applying KMeans to the dataset with the optimal number of cluster
        self.opt_k = Optimal_k
        self.kmeans=KMeans(n_clusters= self.opt_k, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
        y_kmeans = self.kmeans.fit_predict(self.X)
        for i in range(self.opt_k):

            plt.scatter(self.X[y_kmeans == i, 0], self.X[y_kmeans == i,1],s = 80, marker='o', alpha=0.7 , label = 'Cluster {}'.format(i+1))

        plt.scatter(self.kmeans.cluster_centers_[:,0], self.kmeans.cluster_centers_[:,1], s = 100, c = 'black',edgecolors='none', label = 'Centroids')

        # Visualising the clusters
        plt.title('Clusters')
        plt.xlabel('first column')
        plt.ylabel('second column')
        plt.legend()
        plt.show()
        return

# a try :

dataset = Clustering('mall.csv', 3, 4)
dataset.print_elbow(11)
dataset.print_kmeans(5)
