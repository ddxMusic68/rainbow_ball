def rgb_rainbow(frame):
    rgb = [255, 0, 0]
    rgbframe = frame % 256
    if frame <= 255: # red
        rgb[1] += rgbframe
    elif frame <= 255*2: # yellow
        rgb = [255, 255, 0]
        rgb[0] -= rgbframe
    elif frame <= 255*3: # green
        rgb = [0, 255, 0]
        rgb[2] += rgbframe
        rgb[1] -= rgbframe
    elif frame <= 255*3+(255//2) + 3: # blue
        rgb = [0, 0, 255]
        rgb[2] -= rgbframe
        rgb[0] += rgbframe
    elif frame <= 255 * 4:
        rgbframe = rgbframe % 128
        rgb = [128, 0, 127]
        rgb[0] += rgbframe
        rgb[2] -= rgbframe
    return tuple(rgb)

if __name__ == "__main__":
    for i in range(0, 1020):
        print(rgb_rainbow(i))
    print(3.5*255)