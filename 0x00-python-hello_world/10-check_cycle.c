#include "lists"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked lists to check
 *
 * return: 1 if there is a cycle in the list and 0 if not
 */
int check_cycle(listint_ *list)
{
	listint_t *not_speedy = list;
	listint_t *speedy = list;

	if (!list)
		return (0);

	while (not_speedy && speedy && speedy->next)
	{
		not_speedy = not_speedy->next;
		speedy = speedy->next->next;
		if (not_speedy == speedy)
			return (1);
	}
	
	return (0);
}
