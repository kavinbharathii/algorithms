
#[derive(Debug)]
struct NoElementsInList;

struct SinglyLinkedList {
    data: Vec<usize>,
    pointer: usize
}

impl SinglyLinkedList {
    fn new() -> Self {
        SinglyLinkedList {
            data: vec![], 
            pointer: 0
        }
    }

    // implement adding a element
    fn push(&mut self, element: usize) {
        self.data.push(element);
    }

    fn remove(&mut self) {
        self.data.pop();
    }

    fn pushleft(&mut self, element: usize) {
        let mut new_data: Vec<usize> = Vec::new();
        new_data.append(&mut vec![element]);
        new_data.append(&mut self.data);
        self.data = new_data;
    }

    fn popleft(&mut self) {
        self.data = self.data[1..].to_vec();
    }

    fn next(&mut self) -> Result<usize, NoElementsInList> {
        if self.data.len() == 0 {
            Err(NoElementsInList)
        } else {
            if self.pointer == self.data.len() - 1 {
                Ok(self.data[self.pointer])
            } else {
                let value = self.data[self.pointer];
                self.pointer += 1;
                Ok(value)
            }
        }
    }
}

fn main() {
    let mut list = SinglyLinkedList::new();
    list.push(10);
    list.push(30);
    list.pushleft(20);
    list.popleft();
    list.remove();

    let current = list.next().unwrap();
    println!("Current: {:?}", current);
}
