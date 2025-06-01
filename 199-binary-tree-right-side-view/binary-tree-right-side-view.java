import java.util.*;
 
public class Solution {
    
    public List<Integer> rightSideView(TreeNode root) {
        return rightSideView(root, 0, new int[]{-1}, new ArrayList<Integer>());
    }
    
    private List<Integer> rightSideView(TreeNode root, int level, int[] maxLevel, List<Integer> result){
        if(root == null){
            return result;
        }
        if(level > maxLevel[0]){
            result.add(root.val);
            maxLevel[0] = level;
        }
        
        result = rightSideView(root.right, level + 1, maxLevel, result);
        result = rightSideView(root.left, level + 1, maxLevel, result);
        return result;
    }
    
}