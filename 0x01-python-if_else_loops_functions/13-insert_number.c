#include "lists.h"

/**
* insert_node - inserts a number into a sorted signly linked lists
* @head: pointer to a pointer of head of the linked list
* @number: The number to be added
*
* Return: The address of the new node. Otherwise NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;
	/* check if memory allocation was successful */
	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	/* check if memory alloction was successful */
	if (new_node == NULL)
		return (NULL);
	/* set value of new_node to number */
	new_node->n = number;
	/* set next pointer to new_node */
	new_node->next = NULL;
	/**
	 * check if linked list is empty or if provided
	 * number is less that value of the current head
	 */
	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	/* initialize current pointer to head */
	current = *head;
	/**
	 * traverse thru the list to find position to insert new node while
	 * maintaining sorted order
	*/
	while (current->next != NULL && current->next->n < number)
		current = current->next;
	/* insert new node in the appropriate position */
	new_node->next = current->next;
	current->next = new_node;
	/* return address of new node */
	return (new_node);
}
