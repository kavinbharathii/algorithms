
// queue overflow error
#[derive(Debug)]
struct QueueOverflowError;

// queue underflow error
#[derive(Debug)]
struct QueueUnderflowError;

// queue object
struct Queue {
    size: usize,
    data: Vec<usize>
}

impl Queue {
    // Create new queue with size <size>
    fn new(size: usize) -> Self {
        Queue {
            size,
            data: Vec::<usize>::new()
        }
    }

    // Enqueue element to queue
    fn enqueue(&mut self, element: usize) -> Result<&Self, QueueOverflowError> {
        if self.data.len() == self.size {
            Err(QueueOverflowError)
        } else {
            self.data.push(element);
            Ok(self)
        }
    }

    // Dequeue element from queue
    fn dequeue(&mut self) -> Result<&Self, QueueUnderflowError> {
        if self.data.len() == 0 {
            Err(QueueUnderflowError)
        } else {
            self.data.remove(0);
            Ok(self)
        }
    }

    // Display queue
    fn dump(&self) {
        println!("{:?}", self.data);
    }
}

fn main() {
    let mut queue = Queue::new(5);
    queue.enqueue(1).unwrap();
    queue.enqueue(2).unwrap();
    queue.enqueue(3).unwrap();
    queue.enqueue(4).unwrap();
    queue.enqueue(5).unwrap();
    queue.dump();
    queue.dequeue().unwrap();
    queue.dequeue().unwrap();
    queue.dequeue().unwrap();
    queue.dequeue().unwrap();
    queue.dequeue().unwrap();
    queue.dump();
}
