#include "lists.h"

/**
 * check_cycle - check whether a loop exists in a linked list
 *				uses Floyd's algorithm
 *
 * @list: linked list to check
 *
 * Return:	0 if there is no cycle
 *			1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	s = f = list;

	while (s && f)
	{
		s = s->next;
		f = f->next;
		if (f == NULL)
			return (0);
		f = f->next;
		if (f == s)
			return (1);
	}

	if (f == NULL)
		return (0);

	return (1);
}
