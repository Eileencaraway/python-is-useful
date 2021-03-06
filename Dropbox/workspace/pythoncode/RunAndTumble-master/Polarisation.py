import numpy as np
import scipy
from scipy.signal import resample
import matplotlib.pyplot as plt
import os, glob, optparse
from time import time

from persistant_motion_2D_PE_landscape import radial_PE_landscape
from Pressure import filename_par

##=============================================================================

def main():
	"""
	NAME
		Polarisation.py
	
	EXECUTION
		python Polarisation.py [path] [flags]
	
	ARGUMENTS
		histfile	path to density histogram
		dirpath 	path to directory containing histfiles
		
	FLAGS
		-v	--verbose	False
		-s	--show		False
			--nosave	False
		-a	--plotall	False
	"""
	
	me = "Polarisation.main: "
	t0 = time()
	
	## Options
	parser = optparse.OptionParser(conflict_handler="resolve")
	parser.add_option("-s","--show",
		dest="showfig", default=False, action="store_true")
	parser.add_option("-v","--verbose",
		dest="verbose", default=False, action="store_true")
	parser.add_option("--nosave",
		dest="nosave", default=False, action="store_true")
	parser.add_option("-a","--plotall",
		dest="plotall", default=False, action="store_true")
	parser.add_option("-h","--help",
		dest="help", default=False, action="store_true")		
	opt, args = parser.parse_args()
	if opt.help: print main.__doc__; return
	path	= args[0]
	showfig = opt.showfig
	verbose = opt.verbose
	nosave	= opt.nosave
	plotall = opt.plotall
	
	if plotall and os.path.isdir(path):
		showfig = False
		allfiles(path, nosave, verbose)
	elif os.path.isfile(path):
		polarisation_pdf_file(path, nosave, verbose)
	else:
		raise IOError, me+"You gave me rubbish. Abort."
	
	if verbose: print me+"execution time",round(time()-t0,2),"seconds"
	if showfig: plt.show()
	
	return
	
##=============================================================================
def polarisation_pdf_file(histfile, nosave, verbose):
	"""
	Make radial PDF and P(r) plot for a single file
	"""
	me = "Polarisation.polarisation_pdf_file: "
	t0 = time()

	## Filename
	plotfile = os.path.dirname(histfile)+"/POLARr"+os.path.basename(histfile)[6:-4]+".jpg"
	
	## Get pars from filename and convert to R (box size) and tau (memory time)
	a, b = filename_par(histfile, "_alpha"), filename_par(histfile, "_beta")
	R = b
	tau = a*b
	
	## Space (for axes)
	data = np.load(histfile)
	r_bins = data["bin_rad_ang"]
	r = 0.5*(r_bins[:-1]+r_bins[1:])
	th_bins = data["bin_ang"]
	th = 0.5*(th_bins[:-1]+th_bins[1:])
	
	## Load histogram, convert to density, normalise
	H = data["H_ang"]
	rho = (H.T / (2*np.pi*r)).T
	rho /= np.trapz(np.trapz(H,th,axis=1),r,axis=0)

	## Potential
	r_eq = np.linspace(r[0],R+4.0,50*int(R+4.0-r[0]))
	th_eq = th
	U = np.array([radial_PE_landscape(ri, R) for ri in r_eq])
	## Equilibrium density, normalised
	rho_eq = np.exp(-U)[:,np.newaxis].repeat(th_eq.size, axis=1)
	rho_eq /= np.trapz(np.trapz(rho_eq,th_eq,axis=1)*2*np.pi*r_eq,r_eq,axis=0)
			
	##---------------------------------------------------------------			
	## PLOT SET-UP
	
	figtit = "Density and polarisation; quadratic potential; $\\alpha="+str(a)+"$, $\\beta = "+str(b)+"$"
	fsa, fsl, fst = 16,10,16
	
	fig, axs = plt.subplots(3,1,sharex=True)
		
	##---------------------------------------------------------------	
	## PDF PLOT

	ax = axs[0]
	
	ax.plot(r,rho.sum(axis=1),   "b-", label="RTP")
	ax.fill_between(r, 0, rho.sum(axis=1), color="b", alpha=0.1)
	ax.plot(r_eq,rho_eq.sum(axis=1),"r-", label="Eq.")
	ax.fill_between(r_eq, 0, rho_eq.sum(axis=1), color="r", alpha=0.1)
	
	## Accoutrements
	ax.set_xlim([0.0,R+4.0])
	ax.set_ylim(bottom=0.0, top=ax.get_ylim()[1])
	ax.set_ylabel("$\\rho(r,\\phi)$", fontsize=fsa)
	ax.grid()
	
	## Wall
	ax.plot(r_eq, U*ax.get_ylim()[1]/U[-1], "k--", label="$U(r)$")

	##---------------------------------------------------------------
	## POLARISATION
	
	## CALCULATIONS
	m1c, m1s = calc_angular_moment(th,rho,1)
	m2c, m2s = calc_angular_moment(th,rho,2)
	
	m1c_eq, m1s_eq = calc_angular_moment(th_eq,rho_eq,1)
	m2c_eq, m2s_eq = calc_angular_moment(th_eq,rho_eq,2)
	
	## FIRST MOMENT
	ax = axs[1]
	
	## Pressure
	ax.plot(r,m1c, "b-",  label=r"RTP $\langle\cos\theta\rangle(r)$")
	ax.plot(r,m1s, "b--", label=r"RTP $\langle\sin\theta\rangle(r)$")
	ax.plot(r_eq,m1c_eq,"r-",  label=r"Eq. $\langle\cos\theta\rangle(r)$")
	ax.plot(r_eq,m1s_eq,"r--", label=r"Eq. $\langle\sin\theta\rangle(r)$")
	
	## Accoutrements
	ax.set_ylabel("First moments", fontsize=fsa)
	ax.grid()
	ax.legend(loc="lower right",fontsize=fsl)
	
	## Wall
	ax.plot(r_eq, U*ax.get_ylim()[1]/U[-1], "k--", label="$U(r)$")

	## SECOND MOMENT
	ax = axs[2]
	
	## Pressure
	ax.plot(r,m2c, "b-",  label=r"RTP $\langle\cos^2\theta\rangle(r)$")
	ax.plot(r,m2s, "b--", label=r"RTP $\langle\sin^2\theta\rangle(r)$")
	ax.plot(r_eq,m2c_eq,"r-",  label=r"Eq. $\langle\cos^2\theta\rangle(r)$")
	ax.plot(r_eq,m2s_eq,"r--", label=r"Eq. $\langle\sin^2\theta\rangle(r)$")
	
	## Accoutrements
	ax.set_ylabel("Second moments", fontsize=fsa)
	ax.grid()
	ax.legend(loc="lower right",fontsize=fsl)
	
	## Wall
	ax.plot(r_eq, U*ax.get_ylim()[1]/U[-1], "k--", label="$U(r)$")
	
	## Bottom figure
	ax.set_xlabel("$r$", fontsize=fsa)
	
	##---------------------------------------------------------------
	
	## Tidy figure
	fig.suptitle(figtit,fontsize=fst)
	fig.tight_layout();	plt.subplots_adjust(top=0.9)	
	
	if not nosave:
		fig.savefig(plotfile)
		if verbose: print me+"plot saved to",plotfile
	
	return

##=============================================================================
def allfiles(dirpath, nosave, verbose):
	for filepath in np.sort(glob.glob(dirpath+"/*.npz")):
		pressure_pdf_file(filepath, nosave, verbose)
		plt.close()
	return

##=============================================================================

def calc_angular_moment(th,rho,k):
	"""
	Calculate polarisation given density function of coordinate r and body angle th.
	"""
	mkc = np.trapz(rho*np.power(np.cos(th),k),th,axis=1) / np.trapz(rho,th,axis=1)
	mks = np.trapz(rho*np.power(np.sin(th),k),th,axis=1) / np.trapz(rho,th,axis=1)
	return (mkc, mks)
	
## ============================================================================
## ============================================================================
if __name__=="__main__":
	main()