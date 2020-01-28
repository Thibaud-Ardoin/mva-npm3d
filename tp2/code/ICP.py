#
#
#      0===================================0
#      |    TP2 Iterative Closest Point    |
#      0===================================0
#
#
#------------------------------------------------------------------------------------------
#
#      Script of the practical session
#
#------------------------------------------------------------------------------------------
#
#      Hugues THOMAS - 17/01/2018
#


#------------------------------------------------------------------------------------------
#
#          Imports and global variables
#      \**********************************/
#

 
# Import numpy package and name it "np"
import numpy as np

# Import library to plot in python
from matplotlib import pyplot as plt

# Import functions from scikit-learn
from sklearn.neighbors import KDTree

# Import functions to read and write ply files
from utils.ply import write_ply, read_ply
from utils.visu import show_ICP


#------------------------------------------------------------------------------------------
#
#           Functions
#       \***************/
#
#
#   Here you can define usefull functions to be used in the main
#

def RMS(data, ref):
    delta = ref - data
    delta_sq = np.sum(delta**2, axis=0)
    return np.mean(delta_sq)**0.5


def best_rigid_transform(data, ref):
    '''
    Computes the least-squares best-fit transform that maps corresponding points data to ref.
    Inputs :
        data = (d x N) matrix where "N" is the number of points and "d" the dimension
         ref = (d x N) matrix where "N" is the number of points and "d" the dimension
    Returns :
           R = (d x d) rotation matrix
           T = (d x 1) translation vector
           Such that R * data + T is aligned on ref
    '''
    bar_ref = ref.mean(axis=1, keepdims=True)
    bar_data = data.mean(axis=1, keepdims=True)

    Qr = ref - bar_ref
    Qd = data - bar_data

    H = Qd @ Qr.T
    U, S, V = np.linalg.svd(H)

    R = V @ U.T
    if np.linalg.det(R) < 0:
        U[:,2] *= -1
        R = V @ U.T
    R = R
    T = bar_ref - R @ bar_data

    return R, T


def icp_point_to_point(data, ref, max_iter, RMS_threshold):
    '''
    Iterative closest point algorithm with a point to point strategy.
    Inputs :
        data = (d x N_data) matrix where "N_data" is the number of points and "d" the dimension
        ref = (d x N_ref) matrix where "N_ref" is the number of points and "d" the dimension
        max_iter = stop condition on the number of iterations
        RMS_threshold = stop condition on the distance
    Returns :
        data_aligned = data aligned on reference cloud
        R_list = list of the (d x d) rotation matrices found at each iteration
        T_list = list of the (d x 1) translation vectors found at each iteration
        neighbors_list = At each iteration, you search the nearest neighbors of each data point in
        the ref cloud and this obtain a (1 x N_data) array of indices. This is the list of those
        arrays at each iteration
           
    '''

    # Variable for aligned data
    data_aligned = np.copy(data)

    # Initiate lists
    R_list = []
    T_list = []
    neighbors_list = []

    # YOUR CODE

    return data_aligned, R_list, T_list, neighbors_list


#------------------------------------------------------------------------------------------
#
#           Main
#       \**********/
#
#
#   Here you can define the instructions that are called when you execute this file
#


if __name__ == '__main__':
   
    # Transformation estimation
    # *************************
    #

    # If statement to skip this part if wanted
    if True:

        # Cloud paths
        bunny_o_path = '../data/bunny_original.ply'
        bunny_r_path = '../data/bunny_returned.ply'

        # Load point cloud
        data_o = read_ply(bunny_o_path)
        points_o = np.vstack((data_o['x'], data_o['y'], data_o['z']))
        data_r = read_ply(bunny_r_path)
        points_r = np.vstack((data_r['x'], data_r['y'], data_r['z']))

        # Find the best transformation
        R, T = best_rigid_transform(points_r, points_o)

        # Apply the tranformation
        transformed_points = R @ points_r + T

        # Save cloud
        write_ply('../bunny_recaled.ply', [transformed_points.T], ['x', 'y', 'z'])

        # Compute RMS
        RMS1 = RMS(points_r, points_o)
        RMS2 = RMS(transformed_points, points_o)
        # Print RMS
        print("RMS initiale:", RMS1)
        print("RMS après recalage:",RMS2)
   

    # Test ICP and visualize
    # **********************
    #

    # If statement to skip this part if wanted
    if False:

        # Cloud paths
        ref2D_path = '../data/ref2D.ply'
        data2D_path = '../data/data2D.ply'

        # Load clouds

        # Apply ICP

        # Show ICP

    # If statement to skip this part if wanted
    if False:

        # Cloud paths
        bunny_o_path = '../data/bunny_original.ply'
        bunny_p_path = '../data/bunny_perturbed.ply'

        # Load clouds

        # Apply ICP

        # Show ICP


    # Fast ICP
    # ********
    #

    # If statement to skip this part if wanted
    if False:

        # Cloud paths
        NDDC_1_path = '../data/Notre_Dame_Des_Champs_1.ply'
        NDDC_2_path = '../data/Notre_Dame_Des_Champs_2.ply'

        # Load clouds

        # Apply fast ICP for different values of the sampling_limit parameter

        # Plot RMS
        #
        # => To plot something in python use the function plt.plot() to create the figure and 
        #    then plt.show() to display it
