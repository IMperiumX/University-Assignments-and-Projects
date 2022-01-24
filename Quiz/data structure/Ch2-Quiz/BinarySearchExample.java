import java.util.Scanner;

class BinarySearchExample{  
 public static void binarySearch(int arr[], int first, int last, int key){  
   int mid = (first + last)/2;  
   while( first <= last ){  
      if ( arr[mid] < key ){  
        first = mid + 1;     
      }else if ( arr[mid] == key ){  
        System.out.println("Element is found at index: " + mid);  
        break;  
      }else{  
         last = mid - 1;  
      }  
      mid = (first + last)/2;  
   }  
   if ( first > last ){  
      System.out.println("Element is not found!");  
   }  
 }
 public static void main(String args[]){  
        int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        Scanner sc = new Scanner(System.in);
        int key = sc.nextInt(); // User Enter 11 to test binary search should return 5 <-- index of 11
        sc.close();
        int last=arr.length-1;  
        binarySearch(arr,0,last,key);     
 }  
}  