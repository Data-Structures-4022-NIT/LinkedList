class NodeS {
  constructor(data = null) {
    this.data = data;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
  }

  insertInFront(value) {
    const newNode = new NodeS(value);
    newNode.next = this.head;
    this.head = newNode;
  }

  insertInBack(value) {
    const newNode = new NodeS(value);
    if (this.head === null) {
      this.head = newNode;
    } else {
      let p = this.head;
      while (p.next !== null) {
        p = p.next;
      }
      p.next = newNode;
    }
  }

  deleteAtFront() {
    if (this.head === null) {
      return "err";
    }
    const q = this.head;
    this.head = this.head.next;
  }

  deleteAtBack() {
    if (this.head === null) {
      return "err";
    }
    let p = this.head;
    let q = null;
    while (p.next !== null) {
      q = p;
      p = p.next;
    }
    if (q === null) {
      this.head = null;
    } else {
      q.next = null;
    }
  }

  search(val) {
    let p = this.head;
    let index = 0;
    while (p !== null) {
      if (p.data === val) {
        return index;
      }
      index++;
      p = p.next;
    }
    return null;
  }

  clear() {
    this.head = null;
  }

  size() {
    let p = this.head;
    let length = 0;
    while (p !== null) {
      length++;
      p = p.next;
    }
    return length;
  }

  printForward() {
    let p = this.head;
    while (p !== null) {
      console.log(p.data);
      p = p.next;
    }
  }

  printBackward() {
    this.backward(this.head);
  }

  backward(p) {
    if (p === null) {
      return;
    }
    this.backward(p.next);
    console.log(p.data);
  }

  reverseRecursive(p = this.head, isFirst = true) {
    if (p === null) {
      return null;
    }
    const q = this.reverseRecursive(p.next, false);
    if (isFirst) {
      p.next = null;
      this.head = p;
    }
    if (q !== null) {
      q.next = p;
    } else {
      this.head = p;
    }
    return p;
  }

  reverseNonRecursive() {
    let prev = null;
    let current = this.head;
    while (current !== null) {
      const next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }
    this.head = prev;
  }
}

const testS = new SinglyLinkedList();
testS.insertInFront(2);
testS.insertInFront(1);
testS.insertInBack(3);
testS.printForward();
testS.printBackward();
console.log(testS.search(4));
console.log(testS.search(3));
console.log(testS.size());
testS.reverseRecursive();
testS.printForward();
testS.reverseNonRecursive();
testS.printForward();
