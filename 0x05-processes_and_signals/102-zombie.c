#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>


/**
 * infinite_while - Write a C program that creates 5 zombie processes
 *Return: Always 0 (Successful)
 */

int infinite_while(void)
{
	while (1)
		sleep(1);
    
  return (0);
}

/**
 * main - Void
 *Return: Always 0 (Successful)
 */

int main(void)
{

  int b;
	pid_t zombie;

	for (b = 0; b < 5; b++)
	{

    zombie = fork();

    if (!zombie)
    {
			return (0);
    }

		printf("Zombie process created, PID: %d\n", zombie);

  }

  infinite_while();
	return (0);

}
