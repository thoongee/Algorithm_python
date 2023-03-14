import java.util.*;
import java.io.*;

class Node{
  Node left;
  Node right;
  int data;
  
  Node(int data){
    this.data = data;
    left = null;
    right= null;
  }
  
}

class Solution{
  public static void levelOrder(Node root){
	Queue<Node> q = new LinkedList<Node>();
      q.offer(root);
      while(!q.isEmpty()){
          int q_size=  q.size();
          for(int i=0;i<q_size;i++){
              Node cur = q.poll();
              if(cur.left!=null) q.offer(cur.left);
              if(cur.right!=null) q.offer(cur.right);
              System.out.print(cur.data + " ");
          }
      }
	
	}

  public static Node insert(Node root, int data){
    if(root==null){
      return new Node(data);
    }
    else{
      Node cur;
      if(data <= root.data){
        cur = insert(root.left, data);
        root.left = cur;
      }
      else{
        cur = insert(root.right,data);
        root.right =cur;
      }
      return root;
    }
  }
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int t = scan.nextInt();
    Node root = null;
    while(t-- > 0){
      int data = scan.nextInt();
      root = insert(root,data); //트리 쌓기
    }
    scan.close();
    preOrder(root); // inference
  }
}