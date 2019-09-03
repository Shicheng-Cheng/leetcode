```java
public class No3_2 {
    //使用二分搜索，其中在1-n的数字中先分成两半，统计前一半中的数字在数组出现的次数，如果大于n/2，则一定有重复元素。
    public static int find(int [] arr,int length){
        int start=1;
        int end=arr.length-1;
        while(start<=end){
            int middle=(start+end)/2;
            int count= count_num(arr,length,start,middle);
            if(end==start) {
                if (count > 1)
                    return start;
                else {
                    break;
                }
            }
            if(count>middle-start+1){
                end=middle;
            }else {
                start=middle+1;
            }
        }
        return -1;
    }
    public static  int count_num(int[] arr,int length,int start,int end){
        if(arr==null){
            return 0;
        }
        int count=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]>=start && arr[i]<=end){
                ++count;
            }

        }
        return count;
    }
    public static void main(String[] args) {
        int [] arr1={1,3,5,6,2,3,4};
        int length=7;
        int num=find(arr1,length);
        System.out.println(num);
    }
}
```