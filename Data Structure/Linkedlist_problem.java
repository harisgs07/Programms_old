//Second Problem--Deleting Similar kind of elemnts from a sorted LinkedList

//Doubly Link List Problem-
class Linkedlist_problem {

    // User Defined Data Structure called Node named Node
    class Node {
        int data;
        Node next, prev;

        Node(int data) {
            this.data = data;
        }
    }

    public Node head = null; // kind of "object variable" but class type
    public Node tail = null;

    // Set opertaion on Linkede List
    public void setFunction(int data) {

        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
        }
        tail = newNode;
    }

    // Deleting Similar kind of elemnts from a sorted LinkedList
    public void operationDeletion() {

        Node temp = head;
        Node check = null;
        if (temp == null) {
            System.out.println("Empty Container or List");
            return;
        }
        while (temp != null && temp.next != null) {
            check = temp.next;
            while (check != null && check.data == temp.data) {
                check = check.next;
            }
            // System.out.println(check.prev);
            // check.prev = temp;
            temp.next = check;
            temp = temp.next;
        }
    }

    // To display the Linked List
    public void displayLinkedlist() {
        Node temp = head;
        if (temp == null)
            return;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        Linkedlist_problem obj = new Linkedlist_problem();
        obj.setFunction(10);
        obj.setFunction(10);
        obj.setFunction(10);
        obj.setFunction(10);
        obj.setFunction(20);
        obj.setFunction(20);
        obj.setFunction(20);
        obj.setFunction(20);
        obj.setFunction(30);
        obj.setFunction(30);
        obj.setFunction(30);
        obj.setFunction(30);
        obj.setFunction(30);
        obj.setFunction(40);
        obj.setFunction(40);
        obj.setFunction(40);
        obj.setFunction(40);
        obj.setFunction(40);
        obj.setFunction(40);
        obj.setFunction(40);
        obj.setFunction(40);
        obj.displayLinkedlist();
        System.out.println("After The operation the Linkelist will be ");
        obj.operationDeletion();
        obj.displayLinkedlist();
    }
}