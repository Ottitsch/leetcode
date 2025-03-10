import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[][] grid = {
                {0, 1}
        };
        //findMedianSortedArrays(new int[]{3, 2, 1}, new int[]{4, 5, 6});
        System.out.println(islandPerimeter(grid));
    }

    public static List<String> fizzBuzz(int n) {
        List<String> mylist = new ArrayList<>();
        for(int i=0;i<=n;i++){
            if(i%3==0&&i%5==0){
                mylist.add("FizzBuzz");
            } else if(i%3==0){
                mylist.add("Fizz");
            } else if(i%5==0){
                mylist.add("Buzz");
            } else {
                mylist.add(String.valueOf(i));
            }
        }
        return mylist;
    }

    public static int[] plusOne(int[] digits) {
        if(digits[digits.length-1]<9){
            digits[digits.length-1]+=1;
            return digits;
        } else {
            int[] copyOfDigits = new int[digits.length];
            System.arraycopy(digits,0,copyOfDigits,digits.length-1,digits.length);
            copyOfDigits[digits.length-1]+=1;
            return copyOfDigits;
        }
    }

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int complement = target - nums[i];
            if (numMap.containsKey(complement)) {
                return new int[]{numMap.get(complement), i};
            }
            numMap.put(nums[i], i);
        }
        return null;
    }

    public static int romanToInt(String s) {
        Map<Character, Integer> m = new HashMap<>();
        int sum=0;
        m.put('I',1);
        m.put('V',5);
        m.put('X',10);
        m.put('L',50);
        m.put('C',100);
        m.put('D',500);
        m.put('M',1000);

        for(int i=0;i<s.length();i++){
            if (i < s.length() - 1 && m.get(s.charAt(i)) < m.get(s.charAt(i + 1))) {
                sum -= m.get(s.charAt(i));
            } else {
                sum += m.get(s.charAt(i));
            }
        }
        return sum;
    }

    public static int removeElement(int[] nums, int val) {
        int[] returnMe = new int[nums.length];
        int j=0;
        for (int i=0;i<nums.length;i++){
            if(nums[i]!=val)
            {
                returnMe[j]=nums[i];
                j++;
            }
        }
        System.out.println(Arrays.toString(returnMe));
        return j;
    }

    public static boolean containsDuplicate(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int num: nums){
            if(set.contains(num)){
                return true;
            }
            set.add(num);
        }
        return false;
    }

    public static boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> hash1 = new HashMap<>();
        HashMap<Character,Integer> hash2 = new HashMap<>();
        for(char e : s.toCharArray()){
            if(hash1.containsKey(e)){
                hash1.put(e,hash1.get(e)+1);
            } else {
                hash1.put(e,1);
            }
        }
        for(char e : t.toCharArray()){
            if(hash2.containsKey(e)){
                hash2.put(e,hash2.get(e)+1);
            } else {
                hash2.put(e,1);
            }
        }
        return hash1.equals(hash2);
    }

    public static List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);

            map.putIfAbsent(sorted, new ArrayList<>());
            map.get(sorted).add(str);
        }

        return new ArrayList<>(map.values());
    }

    public static int[] getConcatenation(int[] nums) {
        int[] copy = new int[nums.length*2];
        System.arraycopy(nums,0,copy,0,nums.length);
        System.arraycopy(nums,0,copy,nums.length,nums.length);
        return copy;
    }

    public static String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String s1=strs[0];
        String s2=strs[strs.length-1];

        int i=0;
        while (i<s1.length()&&i<s2.length()){
            if(s1.toCharArray()[i]!=s2.toCharArray()[i]){
                break;
            }
            i++;
        }
        return s1.substring(0,i);

    }

    public static int majorityElement(int[] nums) {
        HashMap<Integer,Integer> hashMap = new HashMap();

        for(int num : nums){
            if(hashMap.containsKey(num)){
                hashMap.put(num,hashMap.get(num)+1);
            } else {
                hashMap.put(num,1);
            }
        }
        int key=0;
        int largestValue=0;
        for(Map.Entry<Integer,Integer> entry : hashMap.entrySet()){
            if(entry.getValue()>largestValue){
                key=entry.getKey();
                largestValue=entry.getValue();
            }
        }
        return key;
    }

    public int searchInsert(int[] nums, int target) {

        for(int i = 0;i<nums.length;i++){
            if(nums[i]==target){
                return i;
            }
        }
        for(int i=0;i<nums.length;i++){
            if(i==nums.length-1 && nums[i]<target){
                return i+1;
            }
            else if(nums[i]>target){
                return i;
            }
        }
        return -1;

    }


    public static boolean wordPattern(String pattern, String s) {
        HashMap<Character, String> hashMap = new HashMap<>();
        HashMap<String, Character> reverseMap = new HashMap<>();
        ArrayList<String> sArray = new ArrayList<>();

        int j = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                sArray.add(s.substring(j, i));
                j = i + 1;
            }
        }
        sArray.add(s.substring(j, s.length())); // Fix: use s.length() instead of s.toCharArray().length

        if (sArray.size() != pattern.length()) {
            return false;
        }

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String word = sArray.get(i);

            if (hashMap.containsKey(c)) {
                if (!hashMap.get(c).equals(word)) { // Fix: use .equals() instead of ==
                    return false;
                }
            } else {
                if (reverseMap.containsKey(word)) { // Fix: Prevent different characters from mapping to the same word
                    return false;
                }
                hashMap.put(c, word);
                reverseMap.put(word, c);
            }
        }
        return true;
    }

    public static int scoreOfString(String s) {
        int sum =0;
        int returnable;
        char[] chars = s.toCharArray();
        for (int i = 0;i<chars.length-1;i++){
            returnable = ((int) chars[i]) - ((int) chars[i+1]);
            if(returnable<0){
                returnable = returnable *-1;
            }
            sum+=returnable;
        }
        return sum;
    }

    public static int theMaximumAchievableX(int num, int t) {
        return num + t + t;
    }

    /*public ListNode mergeNodes(ListNode head) {
        head = head.next;
        ListNode start = head;
        while (start != null) {
            ListNode end = start;
            int sum = 0;
            while (end.val != 0) {
                sum += end.val;
                end = end.next;
            }
            start.val = sum;
            start.next = end.next;
            start = start.next;
        }
        return head;
    }*/

    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    private void mergeSort(int[] array, int low, int high) {
        if (low >= high) {
            return;
        }
        int mid = low + (high - low) / 2;
        mergeSort(array, low, mid);
        mergeSort(array, mid + 1, high);
        merge(array, low, mid, high);
    }

    private void merge(int[] array, int low, int mid, int high) {
        int n1 = mid - low + 1;
        int n2 = high - mid;
        int[] leftPart = new int[n1];
        int[] rightPart = new int[n2];

        System.arraycopy(array, low, leftPart, 0, n1);
        System.arraycopy(array, mid + 1, rightPart, 0, n2);

        int p1 = 0, p2 = 0, writeInd = low;
        while (p1 < n1 && p2 < n2) {
            if (leftPart[p1] <= rightPart[p2]) {
                array[writeInd++] = leftPart[p1++];
            } else {
                array[writeInd++] = rightPart[p2++];
            }
        }

        while (p1 < n1) {
            array[writeInd++] = leftPart[p1++];
        }

        while (p2 < n2) {
            array[writeInd++] = rightPart[p2++];
        }
    }

    public static void reverseString(char[] s) {
        for (int i = 0, j = s.length - 1; i < s.length / 2; i++, j--) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
    }

    public static boolean isPalindrome(String s) {
        String check = "";
        for(int i = 0; i<s.length();i++){
            if(Character.isLetterOrDigit(s.charAt(i))){
                check += s.charAt(i);
            }
        }
        check = check.toLowerCase();
        int x = check.length()-1;
        for(int i = 0; i<x; i++){
            if(check.charAt(i)!=check.charAt(x)){
                return false;
            }
            x--;
        }
        return true;
    }

    public String mergeAlternately(String word1, String word2) {
        String str = "";
        for(int i=0;i<word1.length()||i<word2.length();i++){
            if(i<word1.length()){
                str+=word1.toCharArray()[i];
            }
            if(i<word2.length()){
                str+=word2.toCharArray()[i];
            }
        }
        return str;
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int j=0,i=m;j<n;j++) {
            nums1[i] = nums2[j];
            i++;
        }
        Arrays.sort(nums1);
    }

    public int removeDuplicates(int[] nums) {
        int j = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }

    public int maxProfit(int[] prices) {
        int low=prices[0];
        int profit=0;

        for(int i=1;i<prices.length;i++){
            if(low>prices[i]){
                low=prices[i];
            } else if(profit<prices[i]-low){
                profit=prices[i]-low;
            }
        }
        return profit;
    }

    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        Set<Character> charSet = new HashSet<>();
        int left = 0;

        for (int right = 0; right < n; right++) {
            if (!charSet.contains(s.charAt(right))) {
                charSet.add(s.charAt(right));
                maxLength = Math.max(maxLength, right - left + 1);
            } else {
                while (charSet.contains(s.charAt(right))) {
                    charSet.remove(s.charAt(left));
                    left++;
                }
                charSet.add(s.charAt(right));
            }
        }

        return maxLength;
    }

    public int calPoints(String[] operations) {
        Stack<Integer> stack = new Stack<>();

        for (String op : operations) {
            if (op.equals("C")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else if (op.equals("D")) {
                if (!stack.isEmpty()) {
                    stack.push(2 * stack.peek());
                }
            } else if (op.equals("+")) {
                if (stack.size() >= 2) {
                    int first = stack.pop();
                    int second = stack.peek();
                    int sum = first + second;
                    stack.push(first); // Push back the first value
                    stack.push(sum);
                }
            } else {
                stack.push(Integer.parseInt(op));
            }
        }

        int sum = 0;
        for (int score : stack) {
            sum += score;
        }

        return sum;
    }

    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                swap(nums, mid, high);
                high--;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for(char ch: s.toCharArray()) {
            switch (ch) {
                case '(':
                case '{':
                case '[':
                    stack.push(ch);
                    break;
                case ')':
                    if(stack.isEmpty() || stack.pop() != '(') {
                        return false;
                    }
                    break;
                case '}':
                    if(stack.isEmpty() || stack.pop() != '{') {
                        return false;
                    }
                    break;
                case ']':
                    if(stack.isEmpty() || stack.pop() != '[') {
                        return false;
                    }
                    break;
            }
        }

        return stack.isEmpty();
    }

    public String clearDigits(String s) {
        String temp = "";
        for (int i=0;i<s.length();i++){
            if(!Character.isDigit(s.charAt(i))){
                temp+=s.charAt(i);
            } else {
                temp=temp.substring(0,temp.length()-1);
            }

        }
        return temp;
    }

    public int minOperations(String[] logs) {
        Stack<String> stack = new Stack<>();
        for (String s : logs){
            if(s.equals("../")){
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else if(!s.equals("./")){
                stack.push(s);
            }
        }
        return stack.size();
    }

    public static String removeDuplicates(String s) {
        return removeRecursive(s);
    }

    public static String removeRecursive(String s){
        Stack<Character> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        boolean foundDuplicate = false;
        for (int i=0;i<s.length();i++){
            if(!stack.isEmpty()){
                if(stack.peek()!=s.charAt(i)){
                    stack.push(s.charAt(i));
                } else {
                    stack.pop();
                    foundDuplicate=true;
                }
            } else {
                stack.push(s.charAt(i));
            }
        }
        stack.forEach(sb::append);
        if(foundDuplicate==false){
            return sb.toString();
        }
        return removeRecursive(sb.toString());
    }

    public String makeGood(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && Math.abs(c - stack.peek()) == 32) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }

        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.insert(0, stack.pop());
        }

        return result.toString();
    }

    public String removeOuterParentheses(String s) {
        Stack<Character> st=new Stack<>();
        String result="";
        for(int i=0;i<s.length();i++)
        {
            if(st.size()<1 && s.charAt(i)=='(') st.push('(');
            else if(s.charAt(i)=='(')
            {
                result+='(';
                st.push('(');
            }
            else if(st.size()==1 && s.charAt(i)==')') st.pop();
            else
            {
                st.pop();
                result+=')';
            }
        }
        return result;
    }

    public String reversePrefix(String word, char ch) {
        Stack<Character> st=new Stack<>();
        String result="";
        boolean found=false;
        for(char c : word.toCharArray()){
            if(c!=ch){
                st.push(c);
            } else {
                st.push(c);
                found=true;
                break;
            }
        }
        int temp=st.size();
        while (!st.isEmpty()){
            result+=st.pop();
        }
        result += word.substring(temp,word.length());
        if(found==false){
            return word;
        }
        return result;
    }

    public boolean backspaceCompare(String s, String t) {
        Stack<Character> stackS = new Stack<>();
        Stack<Character> stackT = new Stack<>();
        stackS = backspaceCompareHelper(stackS,s);
        stackT= backspaceCompareHelper(stackT,t);
        return stackS.equals(stackT);
    }

    public Stack backspaceCompareHelper(Stack stack,String word){
        for(char c : word.toCharArray()){
            if(c!='#'){
                stack.push(c);
            } else {
                if(!stack.isEmpty()){
                    stack.pop();
                }
            }
        }
        return stack;
    }

    public boolean checkValidString(String s) {
        Stack<Integer> opening = new Stack<>();
        Stack<Integer> flag = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                opening.push(i);
            } else if (c == '*') {
                flag.push(i);
            } else if (c == ')') {
                if (!opening.isEmpty()) {
                    opening.pop();
                } else if (!flag.isEmpty()) {
                    flag.pop();
                } else {
                    return false;
                }
            }
        }

        while (!opening.isEmpty() && !flag.isEmpty()) {
            if (opening.peek() > flag.peek()) {
                return false;
            }
            opening.pop();
            flag.pop();
        }

        return opening.isEmpty();
    }

    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while(start <= end){
            int mid = start + (end - start)/2;

            if(target < nums[mid]){
                end = mid - 1;
            } else if(target > nums[mid]){
                start = mid + 1;
            } else {
                return mid;
            }
        }

        return -1;
    }

    public int guessNumber(int n) {
        int left = 1, right = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;  // Prevents integer overflow
            int result = guess(mid);
            if (result == 0) {  // Found the correct number
                return mid;
            } else if (result == -1) {  // Guess is too high
                right = mid - 1;
            } else {  // Guess is too low
                left = mid + 1;
            }
        }

        return -1;
    }

    public int guess(int n){
        if(n>23){
            return -1;
        }
        if(n<23){
            return 1;
        }
        return 0;
    }

    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, nums, 0, nums1.length);
        System.arraycopy(nums2, 0, nums, nums1.length, nums2.length);
        Arrays.sort(nums);
        if(nums.length%2!=0){
            int temp =nums[nums.length/2]+nums[nums.length/2-1];
            return temp/2+temp%2;
        }
        return nums[nums.length/2];
    }

    public int lengthOfLastWord(String s) {
        int count = 0;
        for(int i = s.length() - 1; i >= 0; i--) {
            if(s.charAt(i) != ' ') {
                count++;
            }
            else if(count > 0) {
                break;
            }
        }
        return count;
    }

    public static int climbStairs(int n) {
        if(n<2){
            return n;
        }
        HashMap<Integer,Integer> hm = new HashMap<Integer, Integer>();
        int i=2;
        if(n>=2){
            hm.put(0,0);
            hm.put(1,1);
            hm.put(2,2);
        }
        while (i<n){
            i++;
            hm.put(i,hm.get(i-1)+hm.get(i-2));
        }
        return hm.get(i);
    }

    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int first = cost[0];
        int second = cost[1];
        if (n<=2) return Math.min(first, second);
        for (int i=2; i<n; i++) {
            int curr = cost[i] + Math.min(first, second);
            first = second;
            second = curr;
        }
        return Math.min(first, second);
    }

    public int tribonacci(int n) {
        if(n<2){
            return n;
        }
        int a=0,b=1,c=1,d;
        while (n-- >2){
            d=c+b+a;
            a=b;
            b=c;
            c=d;
        }
        return c;
    }

    public static int islandPerimeter(int[][] grid) {
        if(grid == null || grid.length == 0)    return 0;
        int sum = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    sum += 4;
                    if(i > 0 && grid[i-1][j] == 1){
                        sum -= 2;
                    }
                    if(j > 0 && grid[i][j-1] == 1){
                        sum -= 2;
                    }
                }
            }
        }
        return sum;
    }


    // STORE INTO HASHMAP
    // THEN AFTERWARDS STORE HASHMAP INTO MINHEAP
    // THEN CONVERT MINHEAP TO int[]
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        for (int i=0;i<nums.length;i++){
            hm.put(nums[i],hm.getOrDefault(nums[i],0)+1);
        }
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(
                Comparator.comparingInt(hm::get)
        );

        for (int key : hm.keySet()) {
            minHeap.add(key);
            if (minHeap.size() > k) {
                minHeap.poll(); // Remove the least frequent element
            }
        }

        return minHeap.stream().mapToInt(Integer::intValue).toArray();
    }


    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        HashSet<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }

        int longestStreak = 0;

        for (int num : numSet) {
            // Only start counting if it's the start of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}

/*
class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}*/

/*class MinStack {
    ArrayList <Integer>min;
    Stack<Integer>stack;
    int sml=Integer.MAX_VALUE;
    public MinStack() {
        this.min=new ArrayList<>();
        this.stack=new Stack<>();
    }

    public void push(int val) {
        if(val<=sml){
            sml=val;
            min.add(val);
        }
        stack.push(val);
    }

    public void pop() {
        if (!stack.isEmpty()) {
            int top = stack.pop();
            if (!min.isEmpty() && top == min.get(min.size() - 1)) {
                min.remove(min.size() - 1);
                sml = min.isEmpty() ? Integer.MAX_VALUE : min.get(min.size() - 1);
            }
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        if(!min.isEmpty())return min.get(min.size()-1);
        return min.get(0);
    }
}*/