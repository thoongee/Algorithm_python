/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        
        // if(root1 != null && root2 != null){
        //     TreeNode root3 = mergeTrees(root1, root2);
        //     root3.val = root1.val + root2.val;
        //     return root3;
        // }
        if (root1==null) return root2;
        if (root2 == null) return root1;

        TreeNode root3 = new TreeNode(root1.val + root2.val);
        root3.left = mergeTrees(root1.left,root2.left);
        root3.right = mergeTrees(root1.right, root2.right);
        return root3;
    
        // if(root1.left != null && root2.left != null){
        //     TreeNode root3.left = mergeTrees(root1.left, root2.left);
        //     root3.left.val = root1.left.val + root2.left.val;
        // }

        // if(root1.right != null && root2.right != null){
        //     TreeNode root3.right = mergeTrees(root1.right, root2.right);
        //     root3.val = root1.right.val+root2.right.val;            
        // }

        // else {
        //     TreeNode root3 = new TreeNode(root1, root2);
        //     return root3;
        // }
        
    }
}