package LeetCode;

public class _27_Remove_Element {
    public static int removeElement(int[] nums, int val) {
        int c = nums.length;
        for (int i = 0; i < c;) {
            if (nums[i] == val) {
                xoaphantu(nums,i);
                c--;
                
            }
           else{
               i++;
           }
        }
        
        return c;   
    }
    
    private static void xoaphantu(int[] nums, int a) {
        for (int i = a+1; i < nums.length; i++) {
            nums[i-1] = nums[i];
        }
    }

    public static void main(String[] args) {
        int[] nums = {3,2,2,3};
        int val = 3;
        
        int temp = removeElement(nums,val);
        for (int i = 0; i < temp; i++) {
            System.out.println(nums[i]);
        }
        System.out.println(temp);
        
    }
}
