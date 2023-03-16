import java.util.*;
import java.io.*;

class Node {
    Node left;
    Node right;
    int data;
    
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {

	/* 
    
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/
	public static void topView(Node root) {
         class NodeObj{    // Each Object holds the current node to add in Queue

            Node node;
            int hd; // Horizontal Distance of each Node
            NodeObj(Node node, int hd)
            {
                this.node = node;
                this.hd = hd;
            }
    
        }  
        if (root == null)
        return;   // There is no top view of of a tree having root null
        
        Queue<NodeObj> queue = new LinkedList<NodeObj>();
        // Declare Map to maintain hd and node data.
        Map<Integer,Integer> topView = new TreeMap<>();
        // We first add the root into the queue along with it's hd 0.
        queue.add(new NodeObj(root, 0));
        
        // Standard level order traversal using Queue
        while (!queue.isEmpty())
        {
            NodeObj curr = queue.poll(); // we dequeue the curent NodeObj
            Node tempNode=curr.node; // get the current node to process.
            int hd=curr.hd;          // get the node's respective horizontal distance.
            
            // if our map does not contain the current node's hd we insert it.
            if (!topView.containsKey(hd))
            {
                topView.put(hd,tempNode.data);
            }
            
            // Now add the left and right child of each node
            // to continue level order traversal
            
            if (tempNode.left != null)
            {
                // hd of left child = hd of parent node - 1.
                queue.add(new NodeObj(tempNode.left, hd - 1));
            }
            
            if (tempNode.right != null)
            {
                // hd of right child = hd of parent node + 1.
                queue.add(new NodeObj(tempNode.right, hd + 1));
            }
        }
        // We just print the values corresponding to each key(hd) or the nodes present in top view
        // loop for printing the values of the node that are visible from the top view  
        for(Integer i : topView.keySet()){ 
            System.out.print(topView.get(i)+" ");
        }

      
    }

	public static Node insert(Node root, int data) {