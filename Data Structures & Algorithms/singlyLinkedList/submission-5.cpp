class ListNode {
public:
    int val;
    ListNode* next = nullptr;

    ListNode(int v) : val(v) {}
};

class LinkedList {
private:
    ListNode* head;
    ListNode* tail;
    int len = 0;

public:
    LinkedList() {
        head = new ListNode(-1);
        tail = new ListNode(-1);
        head->next = tail;
    }

    int get(int index) {
        if (index < 0 || index >= len) {
            return -1;
        }

        ListNode* curr = head->next;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }

    void insertHead(int val) {
        ListNode* node = new ListNode(val);
        node->next = head->next;
        head->next = node;
        len++;
    }
    
    void insertTail(int val) {
        // Find node before tail.
        ListNode* prev = head;
        while (prev->next != tail) {
            prev = prev->next;
        }

        ListNode* node = new ListNode(val);
        prev->next = node;
        node->next = tail;
        len++;
    }

    bool remove(int index) {
        if (index < 0 || index >= len) {
            return false;
        }

        // Find node before removal index.
        ListNode* prev = head;
        for (int i = 0; i < index; i++) {
            prev = prev->next;
        }

        ListNode* deleteNode = prev->next;
        prev->next = deleteNode->next;
        delete deleteNode;

        len--;

        return true;
    }

    vector<int> getValues() {
        vector<int> vals;
        
        ListNode* curr = head->next;
        while (curr && curr != tail) {
            vals.push_back(curr->val);
            curr = curr->next;
        }

        return vals;
    }
};
