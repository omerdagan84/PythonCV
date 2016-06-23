from PIL import Image
from pylab import *

def imresize(im, sz) :
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))

def histeq(im,nbr_bins = 256) :
	imhist, bins = histogram(im.flatten(),nbr_bins,normed=True)
	cdf = imhist.cumsum() # cumulative distribution function
	cdf = 255 * cdf / cdf[-1] # normalize
	# use linear interpolation of cdf to find new pixel values
	im2 = interp(im.flatten(),bins[:-1],cdf)
	return im2.reshape(im.shape), cdf

def compute_average(imlist):
	""" Compute the average of a list of images. """
	# open first image and make into array of type float
	averageim = array(Image.open(imlist[0]), 'f')
	for imname in imlist[1:]:
		try:
			averageim += array(Image.open(imname))
		except:
			print imname + '...skipped'
	averageim /= len(imlist)
	# return average as uint8
	return array(averageim, 'uint8')

def pca(X):
	""" Principal Component Analysis
	input: X, matrix with training data stored as flattened arrays in rows
	return: projection matrix (with important dimensions first), variance and mean.
	"""
	# get dimensions
	num_data,dim = X.shape
	# center data
	mean_X = X.mean(axis=0)
	X = X - mean_X
	if dim > num_data :
		# PCA - compact trick used
		M = dot(X,X.T) # covariance matrix
		e,EV = linalg.eigh(M) # eigenvalues and eigenvectors
		tmp = dot(X.T,EV).T # this is the compact trick
		V = tmp[::-1] # reverse since last eigenvectors are the ones we want
		S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order
		for i in range(V.shape[1]):
			V[:,i] /= S
	else:
		# PCA - SVD used
		U,S,V = linalg.svd(X)
		V = V[:num_data] # only makes sense to return the first num_data
	# return the projection matrix, the variance and the mean
	return V,S,mean_X

def denoise(im,U_init,tolerance=0.1,tau=0.125,tv_weight=100):
	""" An implementation of the Rudin-Osher-Fatemi (ROF) denoising model
	using the numerical procedure presented in eq (11) A. Chambolle (2005).
	Input: noisy input image (grayscale), initial guess for U, weight of
	the TV-regularizing term, steplength, tolerance for stop criterion.
	Output: denoised and detextured image, texture residual. """
	m,n = im.shape #size of noisy image
	# initialize
	U = U_init
	Px = im #x-component to the dual field
	Py = im #y-component of the dual field
	error = 1
	while (error > tolerance):
		Uold = U
		# gradient of primal variable
		GradUx = roll(U,-1,axis=1) - U
		GradUy = roll(U,-1,axis=0) - U
		# update the dual varible
		PxNew = Px + (tau/tv_weight)*GradUx
		PyNew = Py + (tau/tv_weight)*GradUy
		NormNew = maximum(1,sqrt(PxNew**2+PyNew**2))
		Px = PxNew/NormNew # update of x-component (dual)
		Py = PyNew/NormNew # update of y-component (dual)
		# update the primal variable
		RxPx = roll(Px,1,axis=1) # right x-translation of x-component
		RyPy = roll(Py,1,axis=0) # right y-translation of y-component
		DivP = (Px-RxPx)+(Py-RyPy) # divergence of the dual field.
		U = im + tv_weight*DivP # update of the primal variable
		# update of error
		error = linalg.norm(U-Uold)/sqrt(n*m);
	return U,im-U # denoised image and texture residual
