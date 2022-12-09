
// Mergesort algorithm

fn merge_sort(arr: &mut Vec<usize>) -> Vec<usize> {
    if arr.len() <= 1 {
        return arr.to_vec();
    } else {
        let mid = arr.len() / 2;
        let mut left = arr[..mid].to_vec();
        let mut right = arr[mid..].to_vec();

        left = merge_sort(&mut left).to_vec();
        right = merge_sort(&mut right).to_vec();

        let mut l = 0;
        let mut r = 0;
        let mut k = 0;
        
        while (l < left.len()) && (r < right.len()) {
            if left[l] < right[r] {
                arr[k] = left[l];
                l += 1;
                k += 1;
            } else {
                arr[k] = right[r];
                r += 1;
                k += 1;
            }
        } 
        
        while l < left.len() {
            arr[k] = left[l];
            l += 1;
            k += 1;
        }

        while r < right.len() {
            arr[k] = right[r];
            r += 1;
            k += 1;
        }
        
        return arr.to_vec();
    }
}

fn main() {
    let mut a = vec![3, 2, 5, 4, 7, 6, 9, 0, 8, 1];
    merge_sort(&mut a);
    println!("Mergesort : {:?}", a);
}

