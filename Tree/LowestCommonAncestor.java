

	/*
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/
	public static Node lca(Node root, int v1, int v2) {
      	// Write your code here.
        while((root.data-v1)*(root.data-v2)>0){
            root = root.data>v1? root.left:root.right;
        }
        return root;
    }

