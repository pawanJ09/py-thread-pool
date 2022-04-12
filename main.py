from service import scrape
from globals import stocks
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def demo_without_threadpool():
    """
    This method invokes the scraping service in an iterative fashion and calculates the
    processing time.
    :return: None
    """
    start_time = time.perf_counter()
    [scrape.start_scrape(stock) for stock in stocks]
    end_time = time.perf_counter()
    print(f'Total time without thread pool: {end_time - start_time} seconds')


def demo_with_threadpool():
    """
    This method invokes scraping service using ThreadPoolExecutor and calculates the processing
    time.
    :return: None
    """
    # Create Thread pool with 5 threads
    start_time_threads = time.perf_counter()
    executor = ThreadPoolExecutor(max_workers=3)
    # Submit task print_result() with arguments and get a futures object
    futures = [executor.submit(scrape.start_scrape, stock) for stock in stocks]
    # Iterate over all submitted tasks and get results when available however in our case we are
    # printing values in the task
    for future in as_completed(futures):
        pass
        # result = future.result()
        # print(result)
    # Shutdown the thread pool
    executor.shutdown()
    end_time_threads = time.perf_counter()
    print(f'Total time with thread pool: {end_time_threads - start_time_threads} seconds')


if __name__ == '__main__':
    demo_without_threadpool()
    print("="*70)
    demo_with_threadpool()




