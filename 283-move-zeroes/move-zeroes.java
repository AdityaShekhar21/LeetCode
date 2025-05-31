class Solution {
    public void moveZeroes(int[] nums) {
        int insertPos = 0;

        // First, move all non-zero elements to the front
        for (int num : nums) {
            if (num != 0) {
                nums[insertPos++] = num;
            }
        }

        // Then, fill the remaining space with zeros
        while (insertPos < nums.length) {
            nums[insertPos++] = 0;
        }
    }
}
