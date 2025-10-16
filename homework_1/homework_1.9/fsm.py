from enum import Enum
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time


class DigitState(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class SevenSegmentFSM:
    SEGMENTS = {
        DigitState.ZERO:  "abcdef",
        DigitState.ONE:   "bc",
        DigitState.TWO:   "abdeg",
        DigitState.THREE: "abcdg",
        DigitState.FOUR:  "bcfg",
        DigitState.FIVE:  "acdfg",
        DigitState.SIX:   "acdefg",
        DigitState.SEVEN: "abc",
        DigitState.EIGHT: "abcdefg",
        DigitState.NINE:  "abcdfg",
    }

    def __init__(self):
        self.state = DigitState.ZERO

    def next_digit(self):
        new_value = (self.state.value + 1) % 10
        self.state = DigitState(new_value)
        return self.state

    def reset(self):
        self.state = DigitState.ZERO
        return self.state

    def get_segments(self):
        return self.SEGMENTS[self.state]


# ------------------- Visualization Part -------------------

class SevenSegmentDisplay:
    """
    A simple 7-segment visualizer using matplotlib.
    Segments labeled a–g:
       ---a---
      |       |
      f       b
      |       |
       ---g---
      |       |
      e       c
      |       |
       ---d---
    """

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.segments = self._create_segments()

    def _create_segments(self):
        # Each segment is a rectangle patch (positioned manually)
        seg_specs = {
            "a": (0.2, 1.8, 0.6, 0.1),
            "b": (0.9, 1.0, 0.1, 0.8),
            "c": (0.9, 0.1, 0.1, 0.8),
            "d": (0.2, 0.0, 0.6, 0.1),
            "e": (0.1, 0.1, 0.1, 0.8),
            "f": (0.1, 1.0, 0.1, 0.8),
            "g": (0.2, 0.9, 0.6, 0.1),
        }
        segments = {}
        for name, (x, y, w, h) in seg_specs.items():
            rect = patches.Rectangle((x, y), w, h, linewidth=1,
                                     edgecolor='black', facecolor='lightgrey')
            self.ax.add_patch(rect)
            segments[name] = rect
        self.ax.set_xlim(0, 1.2)
        self.ax.set_ylim(0, 2.0)
        return segments

    def update(self, active_segments):
        for name, rect in self.segments.items():
            rect.set_facecolor("red" if name in active_segments else "lightgrey")
        plt.draw()
        plt.pause(0.8)  # Delay for visual effect


# ------------------- Example Simulation -------------------

if __name__ == "__main__":
    fsm = SevenSegmentFSM()
    display = SevenSegmentDisplay()

    plt.ion()  # Turn on interactive mode

    print("7-Segment FSM Visualization Running...")
    for _ in range(12):  # Cycle through digits
        segments_on = fsm.get_segments()
        print(f"Digit {fsm.state.value}: Segments {segments_on}")
        display.update(segments_on)
        fsm.next_digit()

    fsm.reset()
    print("Reset to:", fsm.state)
    plt.ioff()
    plt.show()
