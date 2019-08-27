varres: Variable resolution resampler for InSAR data
-----

var\_res.py is a python implementation of the variable sampler originally written in MATLAB by Mark Simons and Yuri Fialko. Few new improvements include an approximate covariance matrix for the resampled data. The original version of this program was written by Piyush Agram and Romain Jolivet (see http://earthdef.caltech.edu/projects/varres/wiki).

This version was modified by Eric Lindsey to accept GMTSAR results as input (GMT .grd files). Other modifications include a more robust estimation of variance that improves performance, and the addition of an example matlab script for masking out undesired output (the resampler is unstable and sensitive to noise in low-correlation areas, which may require manual intervention).

