#include<stdio.h>
#include<conio.h>
#include<string.h>
struct cricketer{
   char name[50];
   int age;
   int match;
   float avrn;
   char temp;
};
struct cricketer c[20],temp1;
void main() {
   int i,j;
   for(i=0;i<2;i++){
      printf("Enter data of cricketer %d
",i+1);
      //fflush(stdin);
      printf("Name: ");
      gets(c[i].name);
      printf("
Age: ");
      scanf("%d",&c[i].age);
      printf("
Matches: ");
      scanf("%d",&c[i].match);
      printf("

Average runs: ");
      scanf("%f",&c[i].avrn);
      scanf("%c",&c[i].temp);
   }
   /******************/
   /* sorting records */
   /*******************/
   for(i=0;i<2;i++) {
      for(j=i+1;j<2;j++) {
         if(c[i].avrn > c[j].avrn){
            temp1=c[i];
            c[i]=c[j];
            c[j]=temp1;
         }
      }
   }
   printf("Sorted records:
");
   for(i=0;i<2;i++){
      printf("%d\t%s\t%d\t%d\t%f


",i+1,c[i].name,c[i].age,c[i].match,c[i].avrn);
   }
   getch();
}