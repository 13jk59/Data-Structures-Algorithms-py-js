class DequeNode() {
    construtor(val) {
        this.val = val;
        this.next = null;
        this.prev = null; 
    }
}

class Deque {
    constructor() {
        this.head = null;
        this.tail = null; 
    }

    peekFirst() {
        if (this.head) {
            return this.head.val;
        }
        else {
            throw Error("peek in empty deque")
        }
    }

    peekLast() {
        if (this.tail) {
            return this.tail.val;
        }
        else {
            throw Error("peek in empty deque")
        }
    }

    popFirst() {
        if (this.head) {
            const retVal = this.head.val;
            this.head = this.head.next; 
            return retVal;
        }
        else {
            throw Error("pop from empty deque"); 
        }
    }
    
    popLast() {

    }

    addFirst() {

    }

    addLast() {

    }

    length() {
        let length = 0;
        let node = this.head;
        while (node) {
            length++;
            node = node.next; 
        }
        return length; 
    }
}