#include "node.h"

int get_value(struct Node *node)
{
    return node->value;
}

struct Node *get_next_node(struct Node *node)
{
    return node->next_node;
}

void set_value(struct Node *node, int value)
{
    node->value = value;
}

void set_next_node(struct Node *node, struct Node *next)
{
    node->next_node = next;
}