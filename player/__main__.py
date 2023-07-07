import queue
from time import sleep

import mido

from .midi_player import MidiPlayer

if __name__ == "__main__":
    player_mailbox = queue.Queue()
    port_name = "MIDI-file-player"
    midi_player = MidiPlayer(player_mailbox, port_name)

    midi_player.start()
    sleep(1)
    player_mailbox.put("play -f zelda1-dungeon1.mid")

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print("Caught keyboard interrupt. Shutting down.")

    player_mailbox.put("exit")
    midi_player.join()