/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    int max = -1;
    public int[] findFrequentTreeSum(TreeNode root) {
        if(root == null){
            return new int[0];
        }
        populate_sums(root);
        ArrayList<Integer> result = new ArrayList<Integer>();
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            if(entry.getValue() == max){
                result.add(entry.getKey());
            }
        }
        int[] r = new int[result.size()];
       
        for(int i = 0; i < r.length; i++){
            r[i] = result.get(i);
        }
        return r;
    }
    private int populate_sums(TreeNode node){
        int sum = 0;
        if(node.left != null){
            sum += populate_sums(node.left);
        }
        sum += node.val;
        if(node.right != null){
            sum += populate_sums(node.right);
        }
        //System.out.println(sum);
        if(map.containsKey(sum)){
            int i = map.get(sum)+1;
            map.put(sum, i);
            if(i > max){
                max = i;
            }
        }else{
            map.put(sum,1);
            if(1 > max){
                max = 1;
            }
        }
        return sum;
    }