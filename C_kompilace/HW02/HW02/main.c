#include <stdio.h>

#define ERROR_INTERVAL 100

void Positve_evaluate(int input, int *positive, int *negative){ //Counts how many positive or negative numbers go through this function
  if(input > 0)
    *positive += 1;
  else if (a < 0)
    *negative += 1;
}

void Even_evaluate(int input, int *even, int *odd){   //Counts how many even or odd numbers go through this function
  if(input % 2 == 0)
    *even += 1;
  else
    *odd += 1;
}

void Max_find(int input, int *max){   //It compares input number against the max value recorded
  if(input > *max)    //if input is grater than max the max gets updated
    *max = input;
}

void Min_find(int input, int *min){   //It compares input number against the min value recorded
  if(input < *min)    //if input is smaller than min the min gets updated
    *min = input;
}

void Print_output(int number_sum, int positive_sum, int negative_sum, int even_sum, int odd_sum, int add, int max, int min){  //Prints out formated output of the program
  printf("\n");
  printf("Pocet cisel: %d\n", number_sum);
  printf("Pocet kladnych: %d\n", positive_sum);
  printf("Pocet zapornych: %d\n", negative_sum);
  printf("Procento kladnych: %0.2f\n", positive_sum/(number_sum/100.0f)); //Output calculate percentage of positive numbers from total number count
  printf("Procento zapornych: %0.2f\n", negative_sum/(number_sum/100.0f)); //Output calculate percentage of negative numbers from total number count
  printf("Pocet sudych: %d\n", even_sum);
  printf("Pocet lichych: %d\n", odd_sum);
  printf("Procento sudych: %0.2f\n", even_sum/(number_sum/100.0f)); //Output calculate percentage of even numbers from total number count
  printf("Procento lichych: %0.2f\n", odd_sum/(number_sum/100.0f)); //Output calculate percentage of odd numbers from total number count
  printf("Prumer: %0.2f\n", add/(number_sum*1.0f)); //Output counts avarage of inputed numbers
  printf("Maximum: %d\n", max);
  printf("Minimum: %d\n", min);
}

int main(void) {
  int number;
  int err = 0;    //Standard error output
  int first_done = 0; //Switch to check if first number was printed


  int number_sum = 0;
  int positive_sum = 0;
  int negative_sum = 0;
  int even_sum = 0;
  int odd_sum = 0;
  int max = -10000;
  int min = 10000;
  int add = 0;

  while(scanf("%d", &number) != EOF){
    if(number < -10000 || number > 10000) //If input gets out of aproved bounds it prints out error mesage
      {
        err = ERROR_INTERVAL;
        printf("\n");
        printf("Error: Vstup je mimo interval!\n");
        return err;
      }
    else
    {
      if(first_done == 1)   //Checks if first number was printed to correctly print comma
        printf(", ");

      printf("%d",number);  //Prints out inputed number
      number_sum += 1;
      add += number;

      Positve_evaluate(number, &positive_sum, &negative_sum);
      Even_evaluate(number, &even_sum, &odd_sum);
      Max_find(number, &max);
      Min_find(number, &min);
      first_done = 1;
    }
  }
  Print_output(number_sum, positive_sum, negative_sum, even_sum, odd_sum, add, max, min);
  return err;
}
