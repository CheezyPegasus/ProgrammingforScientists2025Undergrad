import multiprocessing
import time

def main():
    print("Parallel and concurrent programming in Python.") 
    # returning is an inherently serial idea; 
    print("Number of cores on this computer:", multiprocessing.cpu_count())
    sum_example_multi_procs()

def sum_example_two_procs():
    # gaussian example
    n = 100;
    data = list(range(1,n+1))
    mid = len(data) // 2

    data_slices = [data[:mid],data[mid+1:]];
    # create stacks/queues
    # stack 
    # queue is like an array/list but it is a safe structure for P.P.
    result_queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target = partial_sum, args = data_slices[0])
    p2 = multiprocessing.Process(target = partial_sum, args = data_slices[1])

    p1.join() # blocking: doesn't process until p1 finishes
    p2.join() # they are both in the queue
    
    # If we care which one goes in first, it needs a value and a label
    # collect code results

    val_1 = result_queue.get()
    val_2 = result_queue.get()

    print(val_1 + val_2)

def sum_example_multi_procs():
    n = 100;
    data = list(range(1,n+1))
    cpus = multiprocessing.cpu_count();

    total = sum_multi_procs(data,cpus)
    # p.start()

def sum_multi_procs(data:list[int],num_procs:int):
    # divide data into equally chunks
    chunk_size = len(data) // num_procs

    data_slices = []

    for i in range(num_procs):
        start  =  i * chunk_size;
        end = (i+1) * chunk_size;
        current_list = data[start:end];
        data_slices.append(current_list)
    
    result_queue = multiprocessing.Queue;

    processes = []

    for slice in data_slices:
        p = multiprocessing.Process(target = partial_sum, args=(slice,result_queue))
        processes.append(p)
        p.start()
        # p.join() oh nononono

    for p in processes:
        p.join() # collect the results;
        # wait for previous ones to finish and then start joining
        # can't make it here until they're all done;

def partial_sum(data_slice:list[int], result_queue:multiprocessing.Queue):
    val = sum(data_slice);
    result_queue.put(val);

if __name__ == "__main__":
    main()
