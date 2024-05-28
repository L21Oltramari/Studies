#include <cs50.h>
#include <math.h>
#include <stdio.h>

int length(long num);
int digit(long num, int i);

int main(void)
{
    // Obtain credit card numbers and length of numbers
    long number = get_long("Number: ");
    int l = length(number);

    // Determine the "second-to-last" total.
    int j;
    int sum1;
    for (j = 2; j <= l; j += 2)
    {
        int d0 = digit(number, j) * 2;
        sum1 = sum1 + digit(d0, 1) + digit(d0, 2);
    }

    // Determine the "left-over" total.
    int sum2;
    for (j = 1; j <= l; j += 2)
    {
        sum2 = sum2 + digit(number, j);
    }

    // Determine the total and look up Luhn's algorithm.
    int final_sum = sum1 + sum2;
    if (final_sum % 10 != 0)
    {
        printf("INVALID\n");
    }
    // Verify the credit card type.
    else
    {
        if (l == 15 && digit(number, 15) == 3 && (digit(number, 14) == 4 || digit(number, 14) == 7))
        {
            printf("AMEX\n");
        }
        else if (l == 16 && digit(number, 16) == 5 && digit(number, 15) >= 1 && digit(number, 15) <= 5)
        {
            printf("MASTERCARD\n");
        }
        else if ((l == 16 && digit(number, 16) == 4) || (l == 13 && digit(number, 13) == 4))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}

// Discover any numbers
int digit(long num, int i)
{
    int d = floor(num % (long) pow(10, i) / (long) pow(10, i - 1));
    return d;
}

// Determine length
int length(long num)
{
    int l;
    for (l = 0; pow(10, l) < num; l++)
    {
    }
    return l;
}
