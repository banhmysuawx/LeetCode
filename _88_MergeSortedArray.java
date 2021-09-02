package LeetCode;

public class _88_MergeSortedArray {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int j : nums2) {
            chenphantu(j, nums1,m);
            //System.out.println("j: "+ j);
            m++;
        }
    }

    private static void chenphantu(int x, int[] nums1, int m) {
        int k=0;
        boolean isInsert = false;
        for (int i = 0 ; i < m; i++) {
            if(nums1[i]>x){
                k=i;
                isInsert = true;
                break;
            }
        }
        //System.out.println("K: "+ k);
        if(isInsert){
            for (int i = m; i > k; i--) {
                nums1[i] = nums1[i-1];
            }
            nums1[k] = x;
        }
        else {
            nums1[m] = x;
        }
    }
    public static void main(String[] args) {
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};
        int m = 3;
        int n = 3;
        merge(nums1, m, nums2, n);
        for (int i : nums1) {
            System.out.println(i);
        }
    }
}