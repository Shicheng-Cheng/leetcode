```java
public boolean find(int target,int[][] arr){
	if(arr==null || arr.length==0 || arr[0].length==0){
		return false;
	}
    int row=0;
    int col=arr[0].length-1;
    while(row<=arr.length-1&&col>=0){
        if(target<arr[row][col]){
            col--;
        }else if(target==arr[row][col]){
            return true;
        }else{
            row++;
        }
    }
    return false;
}
```

