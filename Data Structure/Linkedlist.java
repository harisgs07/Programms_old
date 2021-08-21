public class Linkedlist {

    public class node {

        int data;
        node next;

        node(int data) {
            this.data = data;
        }
    }

    public node head = null;
    public node tail = null;

    public void setfunction(int data) {

        node nextnode = new node(data);
        if (head == null) {
            head = nextnode;
        } else {
            tail.next = nextnode;
        }
        tail = nextnode;
    }

    public void insertfunction(int afterwhat, int data) {

        if (head == null) {
            System.out.println("linked list is Empty We are creating One");
            setfunction(data);
            return;
        }
        node nextnode = new node(data);
        node temp = head;
        while (temp != null && temp.data != afterwhat) {
            temp = temp.next;
        }
        if (temp.next == null) {
            tail.next = nextnode;
            tail = nextnode;
            return;
        }
        nextnode.next = temp.next;
        temp.next = nextnode;
    }

    public void displayfunction() {

        if (head == null) {
            System.out.println("Empty");
            return;
        }
        node temp = head;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    public void delete(int data) {

        if (head == null) {
            System.out.println("It's Empty");
            return;
        }
        node temp = head;
        if (temp != null && temp.data == data) {
            head = temp.next;
            return;
        }
        node prev = null;
        while (temp.data != data) {
            prev = temp;
            temp = temp.next;
        }
        prev.next = temp.next;
    }

    public static void main(String[] args) {

        Linkedlist obj = new Linkedlist();
        obj.displayfunction();
        obj.setfunction(10);
        obj.setfunction(30);
        obj.setfunction(40);
        obj.insertfunction(10, 20);
        obj.setfunction(50);
        obj.displayfunction();
        System.out.println("Performing Delete Operations");
        obj.delete(30);
        obj.displayfunction();

    }
}
