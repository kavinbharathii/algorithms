
// Swapping two elements in a Vector

fn swap(arr: &mut Vec<usize>, a: usize, b: usize) {
    let temp = arr[b];
    arr[b] = arr[a];
    arr[a] = temp;

}

// Bubble sort algorithm

fn bubble_sort(arr: &mut Vec<usize>) {
    for i in 0..arr.len() - 1  {
        for j in 0..arr.len() - i - 1  {
            if arr[j] > arr[j + 1] {
                swap(arr, j, j + 1)
            }
        }
    }
}
  


fn main() {
    let mut a = vec![3, 2, 5, 4, 7, 6, 9, 0, 8, 1];
    bubble_sort(&mut a);
    println!("Bubblesort : {:?}", a);
}

