2013-03-28, tc

Program to create a 1D lattice

Input (file input_lattice1d.dat):
 * nsites
 * bc:
    + bc=0 -> periodic boundary conditions
    + bc=1 -> open boundary conditions

Output (file fort.9):
 * nsites,nbase=1,nk=nsites,maxmulti=2  (\n)
 * for each site
    + site(s) with distance 1           (\n)
    + site(s) with distance 2, if any   (\n)
    + site(s) with distance 3, if any   (\n)
    + ...

NOTE: in the output, the sites are numbered from 1 to nsites
 (this is because then I want to read fort.9 in a fortran 
 program).
