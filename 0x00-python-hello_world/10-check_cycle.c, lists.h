#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: the list to check
 *
 * Return: 0 in case of no cycle, and 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next->next;

		if (tortoise == hare)
			return (1);
	}
	return (0);
}
