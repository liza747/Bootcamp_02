import time, random
from threading import Thread, Lock


class Doctors:
    def __init__(self):
        self.blast = [1 for _ in range(5)]
        self.screwdrivers = [Lock() for _ in range(5)]

    def event(self, i):
        j = (i+1)%5
        while self.blast[i] > 0:
            time.sleep(random.random())
            if not self.screwdrivers[i].locked():
                self.screwdrivers[i].acquire()
                if not self.screwdrivers[j].locked():
                    print(f'Doctor {i+9}: BLAST!')
                    self.screwdrivers[j].acquire()
                    self.blast[i] -= 1
                    self.screwdrivers[j].release()
                    self.screwdrivers[i].release()
                else:
                    self.screwdrivers[i].release()

def run():
    doctor = Doctors()
    doc = [Thread(target=doctor.event, args =(i,)) for i in range(5)]
    for event in doc:
        event.start()
    for event in doc:
        event.join()

if __name__ == '__main__':
    run()