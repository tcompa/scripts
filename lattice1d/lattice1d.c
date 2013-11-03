// 2013-03-28, tc
//
// Program to create a 1D lattice
//
// Input (file input_lattice1d.dat):
//  * nsites
//  * bc:
//     + bc=0 -> periodic boundary conditions
//     + bc=1 -> open boundary conditions
//
// Output (file fort.9):
//  * nsites,nbase=1,nk=nsites,maxmulti=2	(\n)
//  * for each site
//     + site(s) with distance 1		(\n)
//     + site(s) with distance 2, if any	(\n)
//     + site(s) with distance 3, if any	(\n)
//     + ...
//
// NOTE: in the output, the sites are numbered from 1 to nsites
//  (this is because then I want to read fort.9 in a fortran 
//  program).


#include"stdio.h"


// main file
int main(){

int i,j;

// start read input

int bc, nsites;
FILE *fr;
fr=fopen("input_lattice1d.dat","r");
fscanf(fr,"%d",&bc);
fscanf(fr,"%d",&nsites);
printf("\n**********************************************\n");
printf("Total number of sites = %d\n",nsites);
printf("Sites:\n");for(i=0;i<nsites;i++)printf("%d ",i+1);printf("\n");
fclose(fr);

// end read input


// start prepare neighbours list

int ndist;

if(bc==0){
	if(nsites%2==0) ndist=nsites/2;
	else ndist=(nsites-1)/2;
	printf("Independent distances (with PBC) = %d\n",ndist);
}
else{
	ndist=nsites-1;
	printf("Independent distances (with Open BC) = %d\n",ndist);
}
printf("**********************************************\n\n");

int neighb[nsites][ndist][2];
for(i=0;i<nsites;i++)
	for(j=0;j<ndist;j++){
			neighb[i][j][0]=-1;
			neighb[i][j][1]=-1;
		}

int dist,delta;
for(i=0;i<nsites;i++){
	for(j=0;j<nsites;j++){
		if(i!=j){
			delta=abs(i-j);
			if(bc==0) dist=(delta < (nsites-delta)) ? delta : (nsites-delta);
			else      dist=delta;
			if(neighb[i][dist-1][0]==-1) neighb[i][dist-1][0]=j;
			else neighb[i][dist-1][1]=j;
			//printf("%d %d -> %d\n",i,j,dist);
		}
	}
}

// end prepare neighbours list


// start output

FILE *fpneighb, *fpsites;
fpneighb=fopen("fort.9","w");
fprintf(fpneighb,"%d %d %d %d\n",nsites,1,nsites,2); // nsites, nbase, n independent momenta, max multiplicity of a distance

for(i=0;i<nsites;i++){
	printf("site %d\n",i+1);
	for(dist=0;dist<ndist;dist++){
		printf("  dist %d\t",dist+1);
		printf("%d ",neighb[i][dist][0]+1);
		fprintf(fpneighb,"%d ",neighb[i][dist][0]+1);
		if(neighb[i][dist][1]!=-1){
			printf("%d ",neighb[i][dist][1]+1);
			fprintf(fpneighb,"%d ",neighb[i][dist][1]+1);
		}
		printf("\n");
		fprintf(fpneighb,"\n");
	}
}	

fclose(fpneighb);

// end output


return 0;

}
