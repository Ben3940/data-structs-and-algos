#include <stdio.h>
#include "node.h"

int main(void)
{
    struct Node node = {1, NULL};
    struct Node node2 = {2, &node};
    struct Node node3 = {5, NULL};

    printf("%i \n", get_value(&node2));
    printf("%p \n", get_next_node(&node2));
    set_value(&node2, 3);
    printf("%i \n", get_value(&node2));
    set_next_node(&node2, &node3);
    printf("%i \n", get_value(get_next_node(&node2)));

    return 0;
}