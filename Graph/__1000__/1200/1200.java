import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class No {
    String data;
    No left, right;

    No(String data) {
        this.data = data;
    }
}

class BST {
    No root;
    int count = 0;

    void add(String data) {
        No node = new No(data);
        if (root == null) {
            root = node;
            this.count++;
        } else {
            searchNode(root, node);
        }
    }

    boolean search(String data) {
        
        boolean found = searchNodeData(root, data);
        if (found) {
            System.out.println(data + " existe");
        } else {
            System.out.println(data + " nao existe");
        }
        return found;

    }

    boolean searchNodeData(No current, String data) {
        if (current == null) return false;
        if (data.compareTo(current.data) < 0) return searchNodeData(current.left, data);
        if (data.compareTo(current.data) > 0) return searchNodeData(current.right, data);
        return true;
    }

    void searchNode(No current, No node) { 
        if (node.data.compareTo(current.data) < 0) {
            if (current.left == null) {
                current.left = node;
                this.count++;
            } else {
                searchNode(current.left, node);
            }
        } else if (node.data.compareTo(current.data) > 0) {
            if (current.right == null) {
                current.right = node;
                this.count++;
            } else {
                searchNode(current.right, node);
            }
        }
    }

    void InOrder() {
        List<String> nodelist = new ArrayList<>();
        TransverseInOrder(root, nodelist);
        System.out.println(String.join(" ", nodelist));
    }

    void TransverseInOrder(No current, List<String> nodelist) {
        if (current != null) {
            TransverseInOrder(current.left, nodelist);
            nodelist.add(current.data);
            TransverseInOrder(current.right, nodelist);
        }
    }

    void PosOrder() {
        List<String> nodelist = new ArrayList<>();
        TransversePosOrder(root, nodelist);
        System.out.println(String.join(" ", nodelist));
    }

    void TransversePosOrder(No current, List<String> nodelist) {
        if (current != null) {
            TransversePosOrder(current.left, nodelist);
            TransversePosOrder(current.right, nodelist);
            nodelist.add(current.data);
        }
    }

    void PreOrder() {
        List<String> nodelist = new ArrayList<>();
        TransversePreOrder(root, nodelist);
        System.out.println(String.join(" ", nodelist));
    }

    void TransversePreOrder(No current, List<String> nodelist) {
        if (current != null) {
            nodelist.add(current.data);
            TransversePreOrder(current.left, nodelist);
            TransversePreOrder(current.right, nodelist);
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        BST bst = new BST();

        while (input.hasNextLine()) {
            String data = input.nextLine();

            if (data.equals("INFIXA"))
                bst.InOrder();
            else if (data.equals("PREFIXA"))
                bst.PreOrder();
            else if (data.equals("POSFIXA"))
                bst.PosOrder();
            else {
                String[] datas = data.split(" ");
                if (datas[0].equals("P"))
                    bst.search(datas[1]);
                if (datas[0].equals("I"))
                    bst.add(datas[1]);
            }
        }
    }
}
