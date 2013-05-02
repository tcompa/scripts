#include"stdio.h"
#include"stdlib.h"

int main(){

 int alpha,beta,gamma;
 char outfilename[100];

 //read parameters from the input file
 FILE *in_file = fopen("input.dat","r");
 if (in_file == NULL ){
  printf("Error! Could not open input file\n"); 
  return 2;
 } 
 fscanf(in_file,"%d %d",&alpha,&beta);
 //fgets(outfilename,100,in_file);
 fscanf(in_file,"%s",outfilename);
 fclose(in_file);

 //do what you have to do
 gamma=alpha*beta;

 //print output on file
 FILE *out_file = fopen(outfilename,"w");
 fprintf(out_file,"INPUT: alpha=%d, beta=%d\nOUTPUT: gamma=%dx%d=%d\n",alpha,beta,alpha,beta,gamma);
 fclose(out_file); 

 return 0;
}
