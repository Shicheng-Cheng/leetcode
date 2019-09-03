```java

public class No3_1 {
    public static int[] find(int[] arr, int length) {
//        if (arr.length <= 0 && arr == null) {
//            return false;
//        }
//        if (length != arr.length) {
//            return false;
//        }
        int[] arr_new = new int[length - 1];
        int j=0;
        //比较数组第i个数字num与索引i是否相同，若相同，则判断出下一个元素，若不相同，则比较第num个数字，若相同，则找到第一个重复元素，否则两者进行交换。这种方法最多只能找到一种重复元素。
        for (int i = 0; i < arr.length; i++) {
            while (arr[i] != i) {
                if (arr[i] == arr[arr[i]]) {
                    arr_new[j] = arr[i];
                    ++j;
                    return arr_new;
                }
                int swap = arr[i];
                arr[i] = arr[swap];
                arr[swap] = swap;
            }
        }
        return arr_new;
    }
    public static void main(String[] args) {
        int [] arr={0,3,4,5,5,4,1};
        int length=7;
        System.out.println(arr);
        int [] arr1=find(arr,length);
        for(int num:arr1) {
            System.out.println(num);
        }
    }
}
```