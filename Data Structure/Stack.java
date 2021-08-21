public class Stack {

    public class Stacknode {
        int data;
        Stacknode next;

        Stacknode(int data) {
            this.data = data;
        }
    }

    public Stacknode tail = null;
    public Stacknode top = null;

    public void setFunction(int data) {
        Stacknode newNode = new Stacknode(data);
        if (top == null) {
            top = newNode;
            tail = newNode;
            return;
        }
        Stacknode temp = top;
        top = newNode;
        top.next = temp;
    }

    public void deleteFunction() {
        if (top == null) {
            System.out.println("Empty Stack Nothing To Delete Please Performe 'Set Operations'");
            return;
        }
        if (top.next != null)
            top = top.next;
        else
            top = null;
    }

    public void displayFunction() {
        if (top == null) {
            System.out.println("Empty Stack Nothing To Display Please Performe 'Set Operations'");
            return;
        }
        Stacknode temp = top;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        Stack obj = new Stack();
        obj.displayFunction();
        obj.setFunction(10);
        System.out.println("Stack Display");
        obj.displayFunction();
        obj.deleteFunction();
        System.out.println("Delete Display");
        obj.displayFunction();

    }

}
