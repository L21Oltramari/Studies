// In a file called scrabble.c in a folder called scrabble, implement a program in C that 
// determines the winner of a short Scrabble-like game. 
// Your program should prompt for input twice: once for “Player 1” to input their word and once for “Player 2” to input their word. 
// Then, depending on which player scores the most points, your program should either print 
//  “Player 1 wins!”, “Player 2 wins!”, or “Tie!” (in the event the two players score equal points).


#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Points for every letter in the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Obtain the players' input words.
    string word[2];

    word[0] = get_string("Player 1: ");
    word[1] = get_string("Player 2: ");

    // Put both words in score.
    int score1 = compute_score(word[0]);
    int score2 = compute_score(word[1]);

    // To do: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!");
    }

    if (score1 < score2)
    {
        printf("Player 2 wins!");
    }

    else if (score1 == score2)
    {
        printf("Tie!");
    }
}

int compute_score(string word)
{
    // To do: Determine score and return for string, ignore all letter characters
    int score = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }

        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }

    }
    return score;
}
