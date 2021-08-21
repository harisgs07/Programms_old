public class Queue {

    public class Queuenode {
        int data;
        Queuenode next;

        Queuenode(int data) {
            this.data = data;
        }
    }

    public Queuenode end = null;
    public Queuenode top = null;

    public void setFunction(int data) {
        Queuenode newNode = new Queuenode(data);
        if (top == null) {
            top = newNode;
            end = newNode;
            return;
        }
        end.next = newNode;
        end = newNode;
        // System.out.println(top.data);
    }

    public void displayFunction() {
        if (top == null) {
            System.out.println("Empty Queue Nothing To Display");
            return;
        }
        Queuenode temp = top;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    public static void main(String[] args) {
        Queue obj = new Queue();
        // obj.displayFunction();
        obj.setFunction(10);
        obj.setFunction(30);
        obj.setFunction(40);
        obj.setFunction(50);
        System.out.println("Queue Display");
        obj.displayFunction();
    }

}
