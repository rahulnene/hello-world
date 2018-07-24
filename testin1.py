import astropy.cosmology as c
import astropy.units as u



cosmo = c.FlatLambdaCDM(H0=70 * u.km / u.s / u.Mpc, Tcmb0=2.725 * u.K, Om0=0.3)
print(c.WMAP7.critical_density(0))
print(c.Planck15.critical_density(0))




