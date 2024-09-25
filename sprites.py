import pygame


class Sprite:

    def __init__(self, image, frame_width, frame_height, start, end, fps, statename):
        self.frame = 0
        self.frame_timer = 0
        self.state = "idle"
        self.frames = {}
        self.max_frame = {}
        self.framerate = {}
        self.split_image(image, frame_width, frame_height,
                         start, end, fps, statename)

    # Increment the frame once enough time has passed
    def update(self, fps, deltaTime):
        if self.frame_timer > fps / self.framerate[self.state]:
            if self.frame < len(self.frames[self.state]) - 1:
                self.frame += 1
            else:
                self.frame = 0
            self.frame_timer = 0
        else:
            self.frame_timer += deltaTime * 100

    # Change the animation
    def setState(self, state):
        if not state == self.state:
            self.state = state
            self.frame = 0

    # Returns the current frame from the current state
    def getFrame(self):
        return self.frames[self.state][self.frame]

    # Creates the required frames from a spritesheet
    def split_image(self, image, frame_width, frame_height, start, end, fps, statename):
        frames = []
        image_width, image_height = image.get_size()
        for y in range(0, frame_height, image_height):
            for x in range(start, end):
                # Extract a single frame
                if x * frame_width <= image_width and y + frame_height <= image_height:
                    frame = image.subsurface(pygame.Rect(
                        x * frame_width, y, frame_width, frame_height))
                    frames.append(frame)
        self.frames[statename] = frames
        self.framerate[statename] = fps