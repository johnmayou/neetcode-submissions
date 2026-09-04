class DynamicArray {
private:
    int* arr;
    int len = 0;
    int capacity;

public:

    DynamicArray(int capacity) : len(0), capacity(capacity) {
        arr = new int[capacity];
    }

    ~DynamicArray() {
        delete[] arr;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (len == capacity) {
            resize();
        }
        arr[len++] = n;
    }

    int popback() {
        return arr[len-- - 1];
    }

    void resize() {
        capacity *= 2;
        int* newArr = new int[capacity];

        for (int i = 0; i < len; i++) {
            newArr[i] = arr[i];
        }

        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return len;
    }

    int getCapacity() {
        return capacity;
    }
};
