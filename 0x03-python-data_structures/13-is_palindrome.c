#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	listint_t *p; 
	int i, j, *data = NULL, palindrome = 1;

	if (head == NULL || *head == NULL)
		return (1);

	for (j = 0, p = *head; p; p = p->next)
		j++;

	data = malloc(j * sizeof(int));

	for (i = 0, p = *head; p; p = p->next, i++)
		data[i] = p->n;

	for (i = 0, j -= 1; i < j && palindrome; i++, j--)
		palindrome = data[i] == data[j];

	free(data);
	return (palindrome);
}
