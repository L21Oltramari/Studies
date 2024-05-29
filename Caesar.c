// In a file called caesar.c in a folder called caesar
// write a program that enables you to encrypt messages using Caesar’s cipher.
// At the time the user executes the program, they should decide
// by providing a command-line argument, what the key should be in the secret message they’ll provide at runtime.
// We shouldn’t necessarily assume that the user’s key is going to be a number; though you may assume that
//  if it is a number, it will be a positive integer.

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    // Verifies that the program requires two arguments in order to be run.
    if (argc == 2)
    {
        // Makes sure the key in the command line is a positive integer by iterating over it.
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            // Returns an error message if the key contains characters other than numbers.
            if (isdigit(argv[1][i]) == false)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        int k = atoi(argv[1]);

        string plaintext = get_string("plaintext: ");
        printf("ciphertext: ");

        // Translates the plaintext into ciphertext after reading it.
        for (int i = 0; i < strlen(plaintext); i++)
        {
            // Converts every alphabet with lowercase letters.
            if (plaintext[i] >= 'a' && plaintext[i] <= 'z')
            {
                printf("%c", ((((plaintext[i] - 'a') + k) % 26) + 'a'));
            }
            // Converts every alphabet with uppercase letters.
            else if (plaintext[i] >= 'A' && plaintext[i] <= 'Z')
            {
                printf("%c", ((((plaintext[i] - 'A') + k) % 26) + 'A'));
            }
            // Returns any character other than those found in alphabets.
            else
            {
                printf("%c", plaintext[i]);
            }
        }
        printf("\n");
        return 0;
    }
    // Returns an error message (e.g., "./caesar key") if the code is not executed in the correct format.
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}
