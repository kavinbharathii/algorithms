
// Stack overflow error
#[derive(Debug)]
struct StackOverflowError;

// Stack underflow error
#[derive(Debug)]
struct StackUnderflowError;

// Stack object
struct Stack {
    size: usize,
    data: Vec<usize>
}

impl Stack {
    // Create new stack with size <size>
    fn new(size: usize) -> Self {
        Stack {
            size,
            data: Vec::<usize>::new()
        }
    }

    // Push element to stack
    fn push(&mut self, element: usize) -> Result<&Self, StackOverflowError> {
        if self.data.len() == self.size {
            Err(StackOverflowError)
        } else {
            self.data.push(element);
            Ok(self)
        }
    }

    // Pop element from stack
    fn pop(&mut self) -> Result<&Self, StackUnderflowError> {
        if self.data.len() == 0 {
            Err(StackUnderflowError)
        } else {
            self.data.pop();
            Ok(self)
        }
    }

    // Display stack
    fn dump(&self) {
        println!("{:?}", self.data);
    }
}


fn main() {
    let mut stack = Stack::new(5);
    stack.push(1).unwrap();
    stack.push(2).unwrap();
    stack.push(3).unwrap();
    stack.push(4).unwrap();
    stack.push(5).unwrap();
    stack.dump();
    stack.pop().unwrap();
    stack.pop().unwrap();
    stack.pop().unwrap();
    stack.pop().unwrap();
    stack.pop().unwrap();
    stack.dump();
}
