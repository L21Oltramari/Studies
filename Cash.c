#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Find out how much the customer is owed in cents.
    int cents = get_cents();

    // Determine how many quarters you should give the client.
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Determine how many dimes you should give the client.
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Determine how many nickels you should give the client.
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Determine how many cents you should give the client.
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Total coins
    int coins = quarters + dimes + nickels + pennies;

    // Print the entire amount of coins to be given to the client.
    printf("%i\n", coins);
}

int get_cents(void)
{
    // To do
    int no_cents;
    do
    {
        no_cents = get_int("Change owed: ");
    }
    while (no_cents < 0);
    return no_cents;
}

int calculate_quarters(int cents)
{
    // To do
    int quarters = cents / 25;
    return quarters;
}

int calculate_dimes(int cents)
{
    // To do
    int dimes = cents / 10;
    return dimes;
}

int calculate_nickels(int cents)
{
    // To do
    int nickels = cents / 5;
    return nickels;
}

int calculate_pennies(int cents)
{
    // To do
    return cents;
}
