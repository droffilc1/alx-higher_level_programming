#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a is_palindrome
* @head: pointer to pointer of head os a linked lists
*
* Return: 0 if it is not a palindrome. Otherwise 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp;
	listint_t *reversed_list = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = reversed_list;
		reversed_list = temp;
	}

	if (fast)
		slow = slow->next;

	while (reversed_list && slow)
	{
		if (reversed_list->n != slow->n)
			return (0);

		reversed_list = reversed_list->next;
		slow = slow->next;
	}
	return (1);
}
