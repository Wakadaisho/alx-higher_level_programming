#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a node in a list, in order
 *
 * @head: pointer to pointer of start of list
 * @number: integer data to insert in new node
 *
 * Return:	0 if there is no cycle
 *			1 if there is a cycle
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p, *new, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	p = *head;

	if (p == NULL)
	{
		*head = new;
		return (new);
	}

	for (prev = NULL; p; prev = p, p = p->next)
	{
		if (p->n > number)
		{
			new->next = p;
			if (prev == NULL)
			{
				*head = new;
				return (new);
			}
			prev->next = new;
			return (new);
		}
	}

	prev->next = new;
	return (new);
}
