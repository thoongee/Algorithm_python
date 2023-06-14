

	/*
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/
	public static int height(Node root) {
      	// Write your code here.
          int left =0;
          int right = 0;
          if(root.left!=null){
              left = height(root.left)+1;
          }
          if(root.right!=null){
              right = height(root.right)+1;
          }
          if(left<right) return right;
          else return left;
    }

