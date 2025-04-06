import time

def pomodoro_timer(cycles, work_minutes=25, break_minutes=5):
    for cycle in range(1, cycles + 1):
        print ("----------------------")
        print(f"Starting cycle {cycle} of {cycles}")
        print(f"Work for {work_minutes} minutes")
        countdown(work_minutes)

        if cycle < cycles:
            print(f"\n Take a break for {break_minutes} minutes")
            countdown(break_minutes)
        else:
            print("\n Cycles Complete")

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"> {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up")

if __name__ == "__main__":
    try:
        cycle_prompt = input("How many Pomodoro cycles? (1 cycle = 25 min work + 5 min break): ")
        cycles = int(cycle_prompt)
        if cycles < 1:
            raise ValueError
        try:
            pomodoro_timer(cycles)
        except KeyboardInterrupt:
            print("\n Timer canceled")
    except ValueError:
        print("Please enter a valid positive integer")
