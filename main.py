import os;
from typing import *;
import multiprocessing as mp;
import time;
import random;


DELAY = 0.1;
EMPTY_CHAR = " ";


def rand_char():
	return chr(random.randint(33,126));




if __name__ == "__main__":
	screen_widht = os.get_terminal_size().columns;
	streams_len_array:List[int] = [0]*screen_widht;
	buffer:List[str] = [EMPTY_CHAR]*screen_widht;
	while True:
		for index in range(screen_widht):
			current_len = streams_len_array[index];
			if current_len==0:
				streams_len_array[index] = random.choice([random.randint(0,36)]*2 + [0]*200);
				continue;

			if current_len > 0:
				streams_len_array[index] -= 1;
				buffer[index] = rand_char();

		for index in range(len(buffer)):
			print(buffer[index],end="", flush=True);
			buffer[index] = EMPTY_CHAR;


		time.sleep(DELAY);

		


