import time

start_time = time.time()

while True:
    run_time = round(time.time() - start_time)

    hours, remainder = divmod(run_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours:
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        formatted_time = f"{minutes:02}:{seconds:02}"

    print(formatted_time)
    time.sleep(1)