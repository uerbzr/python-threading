import threading
import time

done = False

def worker(text):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1        
        print(f"args:{text} ¬ {counter}")

threading.Thread(target=worker, daemon=True, args=("ABC", )).start()
t2 = threading.Thread(target=worker, daemon=True, args=("DEF", ))
t2.start()

# by joining threads you wont hit below code until worker finishes!

    
input("Press enter to quit")
done = True


