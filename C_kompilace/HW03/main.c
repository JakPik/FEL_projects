#include <stdio.h>

#define ERROR_VSTUP 100
#define ERROR_INTERVAL 101
#define ERROR_SIRKA_LICHOST 102
#define ERROR_VELIKOST_PLOTU 103

//House paterns
#define HOUSE_RIM "X"
#define HOUSE_BASE_FILL " "    //Fill of only house without fence
//Fill paterns
#define MAIN_DIAGONAL_FILL "O"
#define SECOND_DIAGONAL_FILL "*"
//Fence paterns
#define FENCE "|"
#define FENCE_CONNECTION "-"
#define FENCE_NO_CONNECTION " "

// Variables used for house printing
int width;
int hight;
int fence = 0;

// Control variables
int fence_switch = 0;   //Switch for printing fence 0 = no printing
int test;               //Variable for testing if scanf output is valid
int err = 0;            //Variable for defining error statements set for default 0

int input_test(int input, int err);
int interval_test(int input, int err);
int width_test(int input, int err);
int fence_size_test(int input, int hight, int err);
void print_fence(int fence, int *count);
void draw_roof(int j, int i, int roof, int *roof_count);
void print_roof(int roof, int width, int roof_count);
void fill_house(int j, int i, int fence_switch);
void draw_house_rim(int i, int j, int hight, int width, int fence_switch);
void print_house(int roof, int width, int hight, int fence, int fence_switch);

int main(void) {
    test = scanf("%d", &width);
    err = input_test(test, err);
    err = interval_test(width, err);
    err = width_test(width, err);

    if (err != 0)   //Ends the program if the previous checks found any error
        return err;

    test = scanf("%d", &hight);
    err = input_test(test, err);
    err = interval_test(hight, err);

    if (err != 0)
        return err;

    if (width == hight) {
        test = scanf("%d", &fence);
        err = input_test(test, err);
        err = fence_size_test(fence, hight, err);
        fence_switch = 1; //Marks that the house will be printed with a fence
        if (err != 0)
            return err;
    }

    int roof = width / 2 + 1;   //Variable that will calculate the midle of the roof
    print_house(roof, width, hight, fence, fence_switch);
    return 0;
}

int input_test(int input, int err) {    //Tests if the output of scanf is valid or not
    if (input != 1 && err == 0) {   //This condition err == 0 prevents previous error overwrite. Only one error can be written
        fprintf(stderr, "Error: Chybny vstup!\n");
        err = ERROR_VSTUP;
    }
    return err;
}

int interval_test(int input, int err) { //Tests if input is from valid range
    if ((input < 3 || input > 69) && err == 0) {
        fprintf(stderr, "Error: Vstup mimo interval!\n");
        err = ERROR_INTERVAL;
    }
    return err;
}

int width_test(int input, int err) {    //Tests if width is odd number
    if (input % 2 == 0 && err == 0) {
        fprintf(stderr, "Error: Sirka neni liche cislo!\n");
        err = ERROR_SIRKA_LICHOST;
    }
    return err;
}

int fence_size_test(int input, int hight, int err) {    //Tests if fence size in proper range from 0 to less than hight
    if ((input >= hight || input < 1) && err == 0) {
        fprintf(stderr, "Error: Neplatna velikost plotu!\n");
        err = ERROR_VELIKOST_PLOTU;
    }
    return err;
}

void print_fence(int fence, int *count) {   //Prints out fence using the pre set rules
    for (int k = 0; k < fence; k++) {
        if (k % 2 == fence % 2 && (*count == 0 || *count == fence - 1))
            printf(FENCE_CONNECTION);
        else if (k % 2 == fence % 2 && (*count != 0 || *count != fence - 1))
            printf(FENCE_NO_CONNECTION);
        else
            printf(FENCE);
    }
    *count += 1; //Increments count by one to determin what line of fence is currently being printed
}

void draw_roof(int j, int i, int roof, int *roof_count) {    //Draws roof with roof count and proper spaces
    if ((j != roof - i) && (j != roof + i)) //Checks if correct number of roof symbols were printed for current line of printing
        printf(HOUSE_BASE_FILL);
    else {
        printf(HOUSE_RIM);
        *roof_count += 1;
    }
}

void print_roof(int roof, int width, int roof_count) {  //Function for printing roof
    for (int i = 0; i < roof - 1; i++) {
        for (int j = 1; j <= width - 1; j++) {
            if ((i == 0 && roof_count == 1) || (i != 0 && roof_count == 2))
                break;
            draw_roof(j, i, roof, &roof_count);
        }
        roof_count = 0;
        printf("\n");
    }
}

void fill_house(int j, int i, int fence_switch) {   //Prints the filling of the house base on if the fence is being printed or not
    if ((j + i) % 2 == 0 && fence_switch == 1)
        printf(MAIN_DIAGONAL_FILL);
    else if ((j + i) % 2 != 0 && fence_switch == 1)
        printf(SECOND_DIAGONAL_FILL);
    else
        printf(HOUSE_BASE_FILL);
}

void draw_house_rim(int i, int j, int hight, int width, int fence_switch) { //Draws house rim and calls function for its filling
    if ((i == 1) || (i == hight))
        printf(HOUSE_RIM);
    else if ((j == 1) || (j == width))
        printf(HOUSE_RIM);
    else
        fill_house(j, i, fence_switch);
}

void print_house(int roof, int width, int hight, int fence, int fence_switch) { //Print function that takes care of printing all parts of the house
    int fence_count = 0; //Variable that checks how many lines of fence were printed
    int roof_count = 0; //Variable that checks if correct number of roof symbols were printed for coresponding roof line
    print_roof(roof, width, roof_count);

    for (int i = 1; i <= hight; i++) {
        for (int j = 1; j <= width; j++) {
            draw_house_rim(i, j, hight, width, fence_switch);
        }

        if (hight - i < fence)
            print_fence(fence, &fence_count);
        printf("\n");
    }
}
