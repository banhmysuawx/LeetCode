package LeetCode;

public class _1295_FindNumberswithEvenNumberofDigits {
    public static boolean Check(int num){
        int count = 0;
        while(num != 0){
            num = num / 10;
            count++;
        }
        return count % 2 == 0;
    }
    public static int findNumbers(int[] nums) {
        int c = 0;
        /*for (int i = 0; i < nums.length; i++) {
            if (Check(nums[i])) {
                c++;
            }
        }*/
        for (int i : nums) {
            if (Check(i)) {
                c++;
            }
        }

        return c;
    }  
    public static void main(String[] args) {
        int[] nums = {12,345,2,6,7896};
        System.out.println(findNumbers(nums));
    }
}
