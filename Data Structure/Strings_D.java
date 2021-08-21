public class Strings_D {
    String data;

    Strings_D(String data) {
        this.data = data.toLowerCase();
    }

    public String interchange(int addon) {
        char[] data_duplicate = new char[data.length()];
        int value = addon % 26;
        int change;
        for (int i = 0; i < data.length(); i++) {
            // char chtr = data.charAt(i);
            // int a = chtr;
            if (122 - (char) data.charAt(i) < value) {
                change = 96 + value - ((122 - (char) data.charAt(i)) % 122);
                char chtr_reverse = (char) change;
                data_duplicate[i] = chtr_reverse;
            } else {
                change = (char) data.charAt(i) + value;
                char chtr_reverse = (char) change;
                data_duplicate[i] = chtr_reverse;
            }
        }
        String data_duplicate1 = new String(data_duplicate);
        return data_duplicate1;
    }

    public static void main(String[] args) {

        Strings_D obj = new Strings_D("a");
        System.out.println(obj.interchange(34));
        System.out.println(obj.data);

    }

}
