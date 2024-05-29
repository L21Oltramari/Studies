//In a file called readability.c in a folder called readability, you’ll implement a program that
//calculates the approximate grade level needed to comprehend some text.
//Your program should print as output “Grade X” where “X” is the grade level computed, rounded to the nearest integer.
//If the grade level is 16 or higher (equivalent to or greater than a senior undergraduate reading level)
//your program should output “Grade 16+” instead of giving the exact index number.
//If the grade level is less than 1, your program should output “Before Grade 1”.
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void) // int argc, string argv[]
{
    // Compel the user to examine
    string string = get_string("What is the string to analyze? \n");

    int letterCount = 0, wordCount = 0, sentenceCount = 0;

    // Count words, letters and sentences
    // Suppose that a.z. and A.Z. are letters.
    for (int i = 0, stringLength = strlen(string); i < stringLength + 1; i++)
    {
        if ((string[i] >= 'a' && string[i] <= 'z') || (string[i] >= 'A' && string[i] <= 'Z'))
        {
            letterCount++;
        }
        // Any character separated by a space is a word; count the final word at the conclusion of the string.
        if (string[i] == ' ' || string[i] == '\0')
        {
            wordCount++;

        }
        // Upon encountering a ! or ? count as sentence
        if (string[i] == '!' || string[i] == '.'|| string[i] == '?')
        {
            sentenceCount++;
        }

    }

    // Determine the grade reading index
    float averageWordsPer100 = (100 / (float) wordCount) * (float) letterCount;
    float averageSentencePer100 = (100 / (float) wordCount) * (float) sentenceCount;
    int readingIndex = round(0.0588 * averageWordsPer100 - 0.296 * averageSentencePer100 - 15.8);

    if (readingIndex < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (readingIndex > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", readingIndex);
    }

    return 0;
}
