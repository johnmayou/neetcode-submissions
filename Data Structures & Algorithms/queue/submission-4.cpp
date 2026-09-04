class Node {
public:
    int val;
    Node* prev = nullptr;
    Node* next = nullptr;

    Node(int val) : val(val) {}
};

class Deque {
private:
    Node* head;
    Node* tail;

public:
    Deque() {
        head = new Node(-1);
        tail = new Node(-1);
        head->next = tail;
        tail->prev = head;
    }

    bool isEmpty() {
        return head->next == tail;
    }

    void append(int value) {
        Node* pred = tail->prev;
        Node* succ = tail;
        Node* node = new Node(value);
        node->prev = pred;
        node->next = succ;
        pred->next = node;
        succ->prev = node;
    }

    void appendleft(int value) {
        Node* pred = head;
        Node* succ = head->next;
        Node* node = new Node(value);
        node->prev = pred;
        node->next = succ;
        pred->next = node;
        succ->prev = node;
    }

    int pop() {
        if (isEmpty()) return -1;

        Node* pred = tail->prev->prev;
        Node* succ = tail;
        Node* node = pred->next;
        int val = node->val;
        delete node;
        pred->next = succ;
        succ->prev = pred;
        return val;
    }

    int popleft() {
        if (isEmpty()) return -1;

        Node* pred = head;
        Node* succ = head->next->next;
        Node* node = pred->next;
        int val = node->val;
        delete node;
        pred->next = succ;
        succ->prev = pred;
        return val;
    }
};
