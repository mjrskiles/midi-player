import queue
from time import sleep

import mido

from .midi_player import MidiPlayer

if __name__ == "__main__":
    player_mailbox = queue.Queue()
    port_name = "MIDI-file-player"
    midi_player = MidiPlayer(player_mailbox, port_name)
    print(f"Opened MIDI port at {port_name}")

    midi_player.start()
    file_name = input("Enter a MIDI file path: ")
    print(f"Got file path {file_name}")
    player_mailbox.put(f"play -f {file_name}")

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Caught keyboard interrupt. Shutting down.")

    player_mailbox.put("exit")
    midi_player.join()