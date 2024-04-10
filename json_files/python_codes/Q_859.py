##Question ID: 859

#

class MyCircularDeque {
    constructor(k) {
        this.buffer = new Array(k);
        this.front = 0;
        this.rear = 0;
        this.size = 0;
    }

    insertFront(value) {
        if (this.size == this.buffer.length) return false;
        this.front = (this.front - 1 + this.buffer.length) % this.buffer.length;
        this.buffer[this.front] = value;
        this.size++;
        return true;
    }

    insertLast(value) {
        if (this.size == this.buffer.length) return false;
        this.buffer[this.rear] = value;
        this.rear = (this.rear + 1) % this.buffer.length;
        this.size++;
        return true;
    }

    deleteFront() {
        if (this.size == 0) return false;
        this.front = (this.front + 1) % this.buffer.length;
        this.size--;
        return true;
    }

    deleteLast() {
        if (this.size == 0) return false;
        this.rear = (this.rear - 1 + this.buffer.length) % this.buffer.length;
        this.size--;
        return true;
    }

    getFront() {
        if (this.size == 0) return -1;
        return this.buffer[this.front];
    }

    getRear() {
        if (this.size == 0) return -1;
        return this.buffer[(this.rear - 1 + this.buffer.length) % this.buffer.length];
    }

    isEmpty() {
        return this.size == 0;
    }

    isFull() {
        return this.size == this.buffer.length;
    }
}

#
## Structure
#
    # Your code here

#    pass