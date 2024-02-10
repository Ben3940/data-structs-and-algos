struct Node
{
    int value;
    struct Node *next_node;
};

int get_value(struct Node *node);
struct Node *get_next_node(struct Node *node);
void set_value(struct Node *node, int value);
void set_next_node(struct Node *node, struct Node *next);
