
fn quicksort(arr: &mut Vec<usize>) -> Vec<usize> {
    if arr.len() <= 1 {
        return arr.to_vec()
    } else {
        let pivot = arr.pop().expect("No elements in array!");
        let mut left: Vec<usize> = Vec::new();
        let mut right: Vec<usize> = Vec::new();

        for i in 0..arr.len() {
            if arr[i] < pivot {
                left.push(arr[i]);
            } else {
                right.push(arr[i])
            }
        }

        let mut res = quicksort(&mut left);
        res.append(&mut vec![pivot]);
        res.append(&mut quicksort(&mut right));
        return res;

    }
}


fn main() {
    let mut arr: Vec<usize> = vec![9, 8, 7, 6, 5, 4, 3, 2, 1];
    arr = quicksort(&mut arr);
    println!("Sorted array: {:?}", arr);
}

